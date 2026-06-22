import requests
import json
import time
import re
from typing import Optional, Dict, List, Any


class TeraBoxClient:
    """
    TeraBox API Client - Fixed version with correct endpoints and authentication
    """
    
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
        self.base_url = "https://www.terabox.com"
        self.api_url = "https://www.terabox.com/api"
        self.session = requests.Session()
        
        # Required headers - mimic real browser
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Referer": "https://www.terabox.com/",
            "Origin": "https://www.terabox.com",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin"
        })
        
        self.js_token = None
        self.app_id = "250528"
        self.logid = None
        self._login()
    
    def _login(self) -> bool:
        """Login to TeraBox and get session cookies + jsToken"""
        try:
            # Step 1: Get initial cookies and jsToken
            login_url = f"{self.base_url}/login"
            resp = self.session.get(login_url)
            
            # Step 2: Perform actual login
            login_api = f"{self.api_url}/login"
            payload = {
                "email": self.email,
                "password": self.password,
                "app_id": self.app_id
            }
            
            resp = self.session.post(login_api, data=payload)
            data = resp.json()
            
            if data.get("errno") != 0:
                raise Exception(f"Login failed: {data.get('msg', 'Unknown error')}")
            
            # Step 3: Get jsToken from any API call
            self._refresh_js_token()
            
            print(f"✅ Login successful! Welcome {data.get('data', {}).get('name', 'User')}")
            return True
            
        except Exception as e:
            raise Exception(f"Login error: {str(e)}")
    
    def _refresh_js_token(self):
        """Refresh jsToken from server"""
        try:
            test_url = f"{self.api_url}/list?app_id={self.app_id}&path=/"
            resp = self.session.get(test_url)
            data = resp.json()
            
            if data.get("errno") == 0:
                self.js_token = data.get("jsToken", "")
                self.logid = data.get("logid", "")
        except:
            pass
    
    def _get_headers(self) -> Dict[str, str]:
        """Get headers with current jsToken"""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://www.terabox.com/",
            "Origin": "https://www.terabox.com"
        }
        if self.js_token:
            headers["jsToken"] = self.js_token
        return headers
    
    def list_files(self, path: str = "/", limit: int = 100) -> List[Dict[str, Any]]:
        """
        List files and folders from TeraBox
        
        Args:
            path: Folder path (default: "/")
            limit: Max number of items to return
        
        Returns:
            List of file/folder objects
        """
        url = f"{self.api_url}/list"
        params = {
            "app_id": self.app_id,
            "path": path,
            "limit": limit,
            "order": "time",
            "desc": 1
        }
        
        resp = self.session.get(url, params=params, headers=self._get_headers())
        
        if resp.status_code != 200:
            self._refresh_js_token()
            resp = self.session.get(url, params=params, headers=self._get_headers())
        
        data = resp.json()
        
        if data.get("errno") != 0:
            raise Exception(f"List files failed: {data.get('msg', 'Unknown error')}")
        
        return data.get("data", {}).get("list", [])
    
    def upload_file(self, file_path: str, remote_path: str = "/") -> Dict[str, Any]:
        """
        Upload a file to TeraBox
        
        Args:
            file_path: Local file path
            remote_path: Destination folder path (default: "/")
        
        Returns:
            Upload result
        """
        import os
        
        if not os.path.exists(file_path):
            raise Exception(f"File not found: {file_path}")
        
        file_name = os.path.basename(file_path)
        file_size = os.path.getsize(file_path)
        
        # Step 1: Pre-create file
        precreate_url = f"{self.api_url}/precreateFile"
        precreate_data = {
            "app_id": self.app_id,
            "filename": file_name,
            "path": remote_path,
            "size": file_size,
            "uploadid": "",
            "target": "l1"
        }
        
        resp = self.session.post(precreate_url, data=precreate_data, headers=self._get_headers())
        data = resp.json()
        
        if data.get("errno") != 0:
            raise Exception(f"Pre-create failed: {data.get('msg', 'Unknown error')}")
        
        precreate_result = data.get("data", {})
        
        # Check if file already exists (rapid upload)
        if precreate_result.get("return_type") == 2:
            return {"success": True, "message": "File already exists (rapid upload)", "data": precreate_result}
        
        # Step 2: Upload file chunks
        upload_id = precreate_result.get("uploadid")
        chunk_size = 4 * 1024 * 1024  # 4MB chunks
        total_chunks = (file_size + chunk_size - 1) // chunk_size
        
        with open(file_path, 'rb') as f:
            for i in range(total_chunks):
                chunk_data = f.read(chunk_size)
                chunk_start = i * chunk_size
                chunk_end = min(chunk_start + chunk_size, file_size) - 1
                
                upload_url = f"{self.api_url}/upload"
                files = {
                    "file": (file_name, chunk_data, "application/octet-stream")
                }
                params = {
                    "app_id": self.app_id,
                    "path": remote_path,
                    "uploadid": upload_id,
                    "partseq": i + 1
                }
                
                resp = self.session.post(upload_url, params=params, files=files, headers=self._get_headers())
                upload_result = resp.json()
                
                if upload_result.get("errno") != 0:
                    raise Exception(f"Chunk upload failed at {i+1}: {upload_result.get('msg')}")
        
        # Step 3: Create file
        create_url = f"{self.api_url}/createFile"
        create_data = {
            "app_id": self.app_id,
            "path": remote_path,
            "filename": file_name,
            "size": file_size,
            "uploadid": upload_id,
            "target": "l1"
        }
        
        resp = self.session.post(create_url, data=create_data, headers=self._get_headers())
        result = resp.json()
        
        if result.get("errno") != 0:
            raise Exception(f"Create file failed: {result.get('msg', 'Unknown error')}")
        
        return {"success": True, "message": "Upload successful", "data": result.get("data", {})}
    
    def download_file(self, file_id: str) -> bytes:
        """
        Download a file from TeraBox
        
        Args:
            file_id: File ID or fs_id
        
        Returns:
            File content as bytes
        """
        # Get download link
        download_url = f"{self.api_url}/locatedownload"
        params = {
            "app_id": self.app_id,
            "fs_id": file_id,
            "target": "l1"
        }
        
        resp = self.session.get(download_url, params=params, headers=self._get_headers())
        data = resp.json()
        
        if data.get("errno") != 0:
            raise Exception(f"Get download link failed: {data.get('msg', 'Unknown error')}")
        
        dlink = data.get("data", {}).get("dlink")
        if not dlink:
            raise Exception("No download link found")
        
        # Download file
        resp = self.session.get(dlink, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        })
        
        if resp.status_code != 200:
            raise Exception(f"Download failed: {resp.status_code}")
        
        return resp.content
    
    def delete_file(self, file_id: str) -> bool:
        """Delete a file from TeraBox"""
        url = f"{self.api_url}/filemanager"
        payload = {
            "app_id": self.app_id,
            "action": "delete",
            "filelist": json.dumps([file_id]),
            "target": "l1"
        }
        
        resp = self.session.post(url, data=payload, headers=self._get_headers())
        data = resp.json()
        
        if data.get("errno") != 0:
            raise Exception(f"Delete failed: {data.get('msg', 'Unknown error')}")
        
        return True
    
    def create_folder(self, folder_name: str, path: str = "/") -> bool:
        """Create a new folder in TeraBox"""
        url = f"{self.api_url}/filemanager"
        payload = {
            "app_id": self.app_id,
            "action": "mkdir",
            "path": path,
            "name": folder_name,
            "target": "l1"
        }
        
        resp = self.session.post(url, data=payload, headers=self._get_headers())
        data = resp.json()
        
        if data.get("errno") != 0:
            raise Exception(f"Create folder failed: {data.get('msg', 'Unknown error')}")
        
        return True
