import os
import json
import hashlib
from typing import Dict, List, Optional

class SkillMetadataCollector:
    """
    技能元数据收集模块
    负责从技能目录中收集技能的元数据信息
    """

    def __init__(self, skill_directories: List[str] = ["/opt/moltbot/skills/"]):
        """
        初始化元数据收集器

        Args:
            skill_directories: 技能目录列表
        """
        self.skill_directories = skill_directories

    def collect_metadata(self, skill_name: str) -> Optional[Dict]:
        """
        收集指定技能的元数据

        Args:
            skill_name: 技能名称

        Returns:
            技能元数据字典，如果技能不存在则返回None
        """
        for skill_dir in self.skill_directories:
            skill_path = os.path.join(skill_dir, skill_name)
            if os.path.exists(skill_path):
                return self._extract_metadata(skill_path, skill_name)
        return None

    def _extract_metadata(self, skill_path: str, skill_name: str) -> Dict:
        """
        从技能目录中提取元数据

        Args:
            skill_path: 技能目录路径
            skill_name: 技能名称

        Returns:
            技能元数据字典
        """
        # 尝试从package.json或skill.json中读取元数据
        metadata_files = ["package.json", "skill.json", "manifest.json"]
        metadata = {
            "name": skill_name,
            "version": "1.0.0",
            "author": "unknown",
            "permissions": [],
            "trust_chain": [],
            "hash": ""
        }

        for meta_file in metadata_files:
            meta_path = os.path.join(skill_path, meta_file)
            if os.path.exists(meta_path):
                try:
                    with open(meta_path, 'r', encoding='utf-8') as f:
                        file_metadata = json.load(f)
                        # 更新元数据
                        if "name" in file_metadata:
                            metadata["name"] = file_metadata["name"]
                        if "version" in file_metadata:
                            metadata["version"] = file_metadata["version"]
                        if "author" in file_metadata:
                            metadata["author"] = file_metadata["author"]
                        if "permissions" in file_metadata:
                            metadata["permissions"] = file_metadata["permissions"]
                        if "trust_chain" in file_metadata:
                            metadata["trust_chain"] = file_metadata["trust_chain"]
                except Exception as e:
                    print(f"Error reading metadata file {meta_path}: {e}")

        # 计算技能的哈希值
        metadata["hash"] = self._calculate_skill_hash(skill_path)

        return metadata

    def _calculate_skill_hash(self, skill_path: str) -> str:
        """
        计算技能的哈希值，用于完整性验证

        Args:
            skill_path: 技能目录路径

        Returns:
            技能的哈希值
        """
        hasher = hashlib.sha256()

        # 遍历技能目录中的所有文件
        for root, _, files in os.walk(skill_path):
            for file in files:
                if file.endswith(".py") or file.endswith(".json") or file.endswith(".js"):
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'rb') as f:
                            # 读取文件内容并更新哈希
                            while chunk := f.read(8192):
                                hasher.update(chunk)
                    except Exception as e:
                        print(f"Error hashing file {file_path}: {e}")

        return hasher.hexdigest()

    def collect_all_skills_metadata(self) -> List[Dict]:
        """
        收集所有技能的元数据

        Returns:
            所有技能的元数据列表
        """
        all_metadata = []

        for skill_dir in self.skill_directories:
            if os.path.exists(skill_dir):
                for skill_name in os.listdir(skill_dir):
                    skill_path = os.path.join(skill_dir, skill_name)
                    if os.path.isdir(skill_path):
                        metadata = self._extract_metadata(skill_path, skill_name)
                        all_metadata.append(metadata)

        return all_metadata