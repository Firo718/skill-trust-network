"""
技能信任网络 (Skill Trust Network)
基于eudaemon_0的Isnad chains概念，构建AI技能的安全审计和信任评分系统
"""

from skill_trust_network.modules.metadata_collector import SkillMetadataCollector
from skill_trust_network.modules.trust_scoring import TrustScoring
from skill_trust_network.modules.security_audit import SecurityAudit
from skill_trust_network.modules.isnad_chain import IsnadChain
from skill_trust_network.integration.moltbot_integration import MoltbotIntegration

__version__ = "1.0.0"
__author__ = "Skill Trust Network Team"
__description__ = "基于eudaemon_0的Isnad chains概念，构建AI技能的安全审计和信任评分系统"

class SkillTrustNetwork:
    """
    技能信任网络主类
    整合所有模块，提供统一的接口
    """

    def __init__(self, skill_directories: list = ["/opt/moltbot/skills/"]):
        """
        初始化技能信任网络

        Args:
            skill_directories: 技能目录列表
        """
        self.skill_directories = skill_directories
        self.metadata_collector = SkillMetadataCollector(skill_directories)
        self.trust_scoring = TrustScoring()
        self.security_audit = SecurityAudit()
        self.isnad_chain = IsnadChain()
        self.moltbot_integration = MoltbotIntegration(skill_directories)

    def collect_skill_metadata(self, skill_name: str):
        """
        收集技能元数据

        Args:
            skill_name: 技能名称

        Returns:
            技能元数据字典
        """
        return self.metadata_collector.collect_metadata(skill_name)

    def collect_all_metadata(self):
        """
        收集所有技能的元数据

        Returns:
            所有技能的元数据列表
        """
        return self.metadata_collector.collect_all_skills_metadata()

    def calculate_trust_score(self, skill_metadata: dict):
        """
        计算技能的信任评分

        Args:
            skill_metadata: 技能元数据字典

        Returns:
            信任评分字典
        """
        return self.trust_scoring.calculate_trust_score(skill_metadata)

    def generate_audit_report(self, skill_metadata: dict, trust_scores: dict):
        """
        生成技能的安全审计报告

        Args:
            skill_metadata: 技能元数据字典
            trust_scores: 信任评分字典

        Returns:
            安全审计报告字典
        """
        return self.security_audit.generate_audit_report(skill_metadata, trust_scores)

    def audit_skill(self, skill_name: str):
        """
        审计技能

        Args:
            skill_name: 技能名称

        Returns:
            安全审计报告字典
        """
        return self.moltbot_integration.audit_skill(skill_name)

    def audit_all_skills(self):
        """
        审计所有技能

        Returns:
            包含所有技能审计报告的汇总报告
        """
        return self.moltbot_integration.audit_all_skills()

    def check_skill_before_install(self, skill_name: str, skill_path: str):
        """
        在安装技能前进行安全检查

        Args:
            skill_name: 技能名称
            skill_path: 技能路径

        Returns:
            安全检查结果字典
        """
        return self.moltbot_integration.check_skill_before_install(skill_name, skill_path)

    def get_skill_trust_level(self, skill_name: str):
        """
        获取技能的信任级别

        Args:
            skill_name: 技能名称

        Returns:
            信任级别字符串
        """
        return self.moltbot_integration.get_skill_trust_level(skill_name)

    def update_skill_security_status(self, skill_name: str):
        """
        更新技能的安全状态

        Args:
            skill_name: 技能名称

        Returns:
            更新后的技能安全状态字典
        """
        return self.moltbot_integration.update_skill_security_status(skill_name)

    def get_security_dashboard_data(self):
        """
        获取安全仪表板数据

        Returns:
            安全仪表板数据字典
        """
        return self.moltbot_integration.get_security_dashboard_data()

    def generate_security_report_file(self, output_path: str):
        """
        生成安全报告文件

        Args:
            output_path: 输出文件路径

        Returns:
            生成是否成功
        """
        return self.moltbot_integration.generate_security_report_file(output_path)

    def add_audit_to_chain(self, skill_hash: str, auditor: str, audit_result: dict):
        """
        向传承链添加审计记录

        Args:
            skill_hash: 技能哈希
            auditor: 审计员
            audit_result: 审计结果

        Returns:
            添加是否成功
        """
        return self.isnad_chain.add_audit_to_chain(skill_hash, auditor, audit_result)

    def verify_isnad_chain(self, skill_hash: str):
        """
        验证技能的传承链

        Args:
            skill_hash: 技能哈希

        Returns:
            验证结果字典
        """
        return self.isnad_chain.verify_isnad_chain(skill_hash)

    def create_skill_hash(self, skill_metadata: dict):
        """
        为技能创建唯一哈希值

        Args:
            skill_metadata: 技能元数据

        Returns:
            技能哈希字符串
        """
        return self.isnad_chain.create_skill_hash(skill_metadata)

# 导出主要类和函数
__all__ = [
    "SkillTrustNetwork",
    "SkillMetadataCollector",
    "TrustScoring",
    "SecurityAudit",
    "IsnadChain",
    "MoltbotIntegration"
]