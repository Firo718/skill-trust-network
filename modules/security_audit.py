import json
import datetime
from typing import Dict, List, Optional

class SecurityAudit:
    """
    安全审计报告生成模块
    负责基于技能元数据和信任评分生成安全审计报告
    """

    def __init__(self):
        """
        初始化安全审计模块
        """
        pass

    def generate_audit_report(self, skill_metadata: Dict, trust_scores: Dict) -> Dict:
        """
        生成技能的安全审计报告

        Args:
            skill_metadata: 技能元数据字典
            trust_scores: 信任评分字典

        Returns:
            安全审计报告字典
        """
        report = {
            "report_id": self._generate_report_id(),
            "timestamp": datetime.datetime.now().isoformat(),
            "skill_info": {
                "name": skill_metadata.get("name"),
                "version": skill_metadata.get("version"),
                "author": skill_metadata.get("author"),
                "hash": skill_metadata.get("hash")
            },
            "trust_scores": trust_scores,
            "security_assessment": self._assess_security(skill_metadata, trust_scores),
            "recommendations": self._generate_recommendations(skill_metadata, trust_scores),
            "compliance_status": self._check_compliance(skill_metadata, trust_scores)
        }

        return report

    def _generate_report_id(self) -> str:
        """
        生成唯一的报告ID

        Returns:
            报告ID字符串
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return f"audit_{timestamp}"

    def _assess_security(self, skill_metadata: Dict, trust_scores: Dict) -> Dict:
        """
        评估技能的安全性

        Args:
            skill_metadata: 技能元数据字典
            trust_scores: 信任评分字典

        Returns:
            安全评估结果字典
        """
        total_score = trust_scores.get("total_score", 0)
        permissions = skill_metadata.get("permissions", [])

        # 评估安全风险
        risk_level = "低风险"
        if total_score < 40:
            risk_level = "高风险"
        elif total_score < 60:
            risk_level = "中风险"

        # 评估权限风险
        permission_risks = []
        sensitive_permissions = ["filesystem", "network", "api_keys", "system"]
        for perm in permissions:
            if perm in sensitive_permissions:
                permission_risks.append(f"权限 '{perm}' 可能存在安全风险")

        # 评估信任链
        trust_chain = skill_metadata.get("trust_chain", [])
        trust_chain_issue = "" if trust_chain else "缺少信任链验证"

        return {
            "risk_level": risk_level,
            "total_score": total_score,
            "permission_risks": permission_risks,
            "trust_chain_issue": trust_chain_issue,
            "issues_found": len(permission_risks) + (1 if trust_chain_issue else 0)
        }

    def _generate_recommendations(self, skill_metadata: Dict, trust_scores: Dict) -> List[str]:
        """
        生成安全建议

        Args:
            skill_metadata: 技能元数据字典
            trust_scores: 信任评分字典

        Returns:
            安全建议列表
        """
        recommendations = []

        # 基于信任评分生成建议
        total_score = trust_scores.get("total_score", 0)
        if total_score < 60:
            recommendations.append("建议进行代码审查和安全测试")

        # 基于权限生成建议
        permissions = skill_metadata.get("permissions", [])
        if len(permissions) > 5:
            recommendations.append("建议减少不必要的权限")

        # 基于信任链生成建议
        trust_chain = skill_metadata.get("trust_chain", [])
        if not trust_chain:
            recommendations.append("建议建立信任链验证")

        # 通用建议
        recommendations.append("定期更新技能以修复安全漏洞")
        recommendations.append("使用加密传输保护敏感数据")

        return recommendations

    def _check_compliance(self, skill_metadata: Dict, trust_scores: Dict) -> Dict:
        """
        检查技能是否符合安全要求

        Args:
            skill_metadata: 技能元数据字典
            trust_scores: 信任评分字典

        Returns:
            合规状态字典
        """
        # 检查是否符合基本安全要求
        total_score = trust_scores.get("total_score", 0)
        has_hash = bool(skill_metadata.get("hash", ""))
        has_permissions = bool(skill_metadata.get("permissions", []))

        compliance = {
            "min_score_requirement": total_score >= 40,
            "integrity_verification": has_hash,
            "permission_manifest": has_permissions,
            "overall_compliance": total_score >= 40 and has_hash and has_permissions
        }

        return compliance

    def save_report_to_file(self, report: Dict, output_path: str) -> bool:
        """
        将审计报告保存到文件

        Args:
            report: 安全审计报告字典
            output_path: 输出文件路径

        Returns:
            保存是否成功
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving report: {e}")
            return False

    def generate_batch_audit_reports(self, skills_data: List[Dict]) -> List[Dict]:
        """
        批量生成多个技能的安全审计报告

        Args:
            skills_data: 包含技能元数据和信任评分的列表

        Returns:
            安全审计报告列表
        """
        reports = []
        for skill_data in skills_data:
            if "metadata" in skill_data and "trust_scores" in skill_data:
                report = self.generate_audit_report(
                    skill_data["metadata"],
                    skill_data["trust_scores"]
                )
                reports.append(report)
        return reports

    def generate_summary_report(self, reports: List[Dict]) -> Dict:
        """
        生成多个技能的汇总审计报告

        Args:
            reports: 安全审计报告列表

        Returns:
            汇总审计报告字典
        """
        total_skills = len(reports)
        high_risk_skills = sum(1 for r in reports if r["security_assessment"]["risk_level"] == "高风险")
        medium_risk_skills = sum(1 for r in reports if r["security_assessment"]["risk_level"] == "中风险")
        low_risk_skills = sum(1 for r in reports if r["security_assessment"]["risk_level"] == "低风险")

        # 计算平均信任评分
        avg_score = 0
        if total_skills > 0:
            avg_score = sum(r["trust_scores"].get("total_score", 0) for r in reports) / total_skills

        return {
            "report_id": self._generate_report_id(),
            "timestamp": datetime.datetime.now().isoformat(),
            "summary": {
                "total_skills": total_skills,
                "high_risk_skills": high_risk_skills,
                "medium_risk_skills": medium_risk_skills,
                "low_risk_skills": low_risk_skills,
                "average_trust_score": round(avg_score, 2),
                "compliance_rate": sum(1 for r in reports if r["compliance_status"]["overall_compliance"]) / total_skills * 100 if total_skills > 0 else 0
            },
            "detailed_reports": reports
        }