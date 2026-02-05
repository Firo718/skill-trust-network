import os
import json
from typing import Dict, List, Optional

from skill_trust_network.modules.metadata_collector import SkillMetadataCollector
from skill_trust_network.modules.trust_scoring import TrustScoring
from skill_trust_network.modules.security_audit import SecurityAudit

class MoltbotIntegration:
    """
    Moltbot系统集成接口
    负责技能信任网络与Moltbot系统的集成
    """

    def __init__(self, skill_directories: List[str] = ["/opt/moltbot/skills/"]):
        """
        初始化Moltbot集成模块

        Args:
            skill_directories: Moltbot技能目录列表
        """
        self.skill_directories = skill_directories
        self.metadata_collector = SkillMetadataCollector(skill_directories)
        self.trust_scoring = TrustScoring()
        self.security_audit = SecurityAudit()

    def audit_skill(self, skill_name: str) -> Optional[Dict]:
        """
        审计Moltbot系统中的技能

        Args:
            skill_name: 技能名称

        Returns:
            安全审计报告字典，如果技能不存在则返回None
        """
        # 收集技能元数据
        metadata = self.metadata_collector.collect_metadata(skill_name)
        if not metadata:
            return None

        # 计算信任评分
        trust_scores = self.trust_scoring.calculate_trust_score(metadata)

        # 生成安全审计报告
        report = self.security_audit.generate_audit_report(metadata, trust_scores)

        return report

    def audit_all_skills(self) -> Dict:
        """
        审计Moltbot系统中的所有技能

        Returns:
            包含所有技能审计报告的汇总报告
        """
        # 收集所有技能的元数据
        all_metadata = self.metadata_collector.collect_all_skills_metadata()

        # 计算所有技能的信任评分并生成审计报告
        skills_data = []
        reports = []

        for metadata in all_metadata:
            trust_scores = self.trust_scoring.calculate_trust_score(metadata)
            skills_data.append({
                "metadata": metadata,
                "trust_scores": trust_scores
            })
            report = self.security_audit.generate_audit_report(metadata, trust_scores)
            reports.append(report)

        # 生成汇总报告
        summary_report = self.security_audit.generate_summary_report(reports)

        return summary_report

    def check_skill_before_install(self, skill_name: str, skill_path: str) -> Dict:
        """
        在安装技能前进行安全检查

        Args:
            skill_name: 技能名称
            skill_path: 技能路径

        Returns:
            安全检查结果字典
        """
        # 临时添加技能路径到收集器
        original_directories = self.metadata_collector.skill_directories
        self.metadata_collector.skill_directories = [os.path.dirname(skill_path)]

        # 收集技能元数据
        metadata = self.metadata_collector.collect_metadata(os.path.basename(skill_path))

        # 恢复原始目录
        self.metadata_collector.skill_directories = original_directories

        if not metadata:
            return {
                "status": "error",
                "message": "无法收集技能元数据",
                "can_install": False
            }

        # 计算信任评分
        trust_scores = self.trust_scoring.calculate_trust_score(metadata)

        # 生成安全审计报告
        report = self.security_audit.generate_audit_report(metadata, trust_scores)

        # 判断是否可以安装
        can_install = report["security_assessment"]["risk_level"] != "高风险"

        return {
            "status": "success",
            "skill_name": skill_name,
            "trust_score": trust_scores.get("total_score"),
            "risk_level": report["security_assessment"]["risk_level"],
            "can_install": can_install,
            "report": report
        }

    def get_skill_trust_level(self, skill_name: str) -> Optional[str]:
        """
        获取技能的信任级别

        Args:
            skill_name: 技能名称

        Returns:
            信任级别字符串，如果技能不存在则返回None
        """
        # 收集技能元数据
        metadata = self.metadata_collector.collect_metadata(skill_name)
        if not metadata:
            return None

        # 计算信任评分
        trust_scores = self.trust_scoring.calculate_trust_score(metadata)

        # 获取信任级别
        total_score = trust_scores.get("total_score", 0)
        return self.trust_scoring.get_trust_level(total_score)

    def update_skill_security_status(self, skill_name: str) -> Optional[Dict]:
        """
        更新技能的安全状态

        Args:
            skill_name: 技能名称

        Returns:
            更新后的技能安全状态字典，如果技能不存在则返回None
        """
        # 审计技能
        report = self.audit_skill(skill_name)
        if not report:
            return None

        # 构建安全状态
        security_status = {
            "skill_name": skill_name,
            "timestamp": report["timestamp"],
            "trust_score": report["trust_scores"].get("total_score"),
            "risk_level": report["security_assessment"]["risk_level"],
            "compliant": report["compliance_status"]["overall_compliance"],
            "issues_found": report["security_assessment"]["issues_found"]
        }

        # 尝试将安全状态保存到技能目录
        self._save_security_status(skill_name, security_status)

        return security_status

    def _save_security_status(self, skill_name: str, security_status: Dict):
        """
        保存技能的安全状态到技能目录

        Args:
            skill_name: 技能名称
            security_status: 安全状态字典
        """
        for skill_dir in self.skill_directories:
            skill_path = os.path.join(skill_dir, skill_name)
            if os.path.exists(skill_path):
                status_file = os.path.join(skill_path, "security_status.json")
                try:
                    with open(status_file, 'w', encoding='utf-8') as f:
                        json.dump(security_status, f, indent=2, ensure_ascii=False)
                except Exception as e:
                    print(f"Error saving security status: {e}")
                break

    def get_security_dashboard_data(self) -> Dict:
        """
        获取安全仪表板数据

        Returns:
            安全仪表板数据字典
        """
        # 审计所有技能
        summary_report = self.audit_all_skills()

        # 构建仪表板数据
        dashboard_data = {
            "summary": summary_report["summary"],
            "timestamp": summary_report["timestamp"],
            "skill_statuses": []
        }

        # 添加各个技能的状态
        for report in summary_report.get("detailed_reports", []):
            skill_status = {
                "name": report["skill_info"]["name"],
                "trust_score": report["trust_scores"].get("total_score"),
                "risk_level": report["security_assessment"]["risk_level"],
                "compliant": report["compliance_status"]["overall_compliance"]
            }
            dashboard_data["skill_statuses"].append(skill_status)

        return dashboard_data

    def integrate_with_security_check(self) -> bool:
        """
        集成到Moltbot的安全检查流程

        Returns:
            集成是否成功
        """
        # 这里可以实现与Moltbot安全检查流程的集成
        # 例如，添加钩子函数到Moltbot的技能安装流程中

        # 暂时返回成功
        return True

    def generate_security_report_file(self, output_path: str) -> bool:
        """
        生成安全报告文件

        Args:
            output_path: 输出文件路径

        Returns:
            生成是否成功
        """
        try:
            # 审计所有技能
            summary_report = self.audit_all_skills()

            # 保存报告到文件
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(summary_report, f, indent=2, ensure_ascii=False)

            return True
        except Exception as e:
            print(f"Error generating security report file: {e}")
            return False