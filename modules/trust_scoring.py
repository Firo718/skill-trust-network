from typing import Dict, List, Optional

class TrustScoring:
    """
    信任评分计算模块
    负责计算技能的信任评分，基于多个因素
    """

    def __init__(self):
        """
        初始化信任评分计算器
        """
        # 各因素的权重
        self.weights = {
            "author_reputation": 0.2,
            "community_audit": 0.25,
            "usage_history": 0.2,
            "permission_reasonableness": 0.2,
            "code_quality": 0.15
        }

    def calculate_trust_score(self, skill_metadata: Dict) -> Dict:
        """
        计算技能的信任评分

        Args:
            skill_metadata: 技能元数据字典

        Returns:
            包含各因素评分和总评分的字典
        """
        # 计算各因素的评分
        scores = {
            "author_reputation": self._calculate_author_reputation(skill_metadata),
            "community_audit": self._calculate_community_audit(skill_metadata),
            "usage_history": self._calculate_usage_history(skill_metadata),
            "permission_reasonableness": self._calculate_permission_reasonableness(skill_metadata),
            "code_quality": self._calculate_code_quality(skill_metadata)
        }

        # 计算总评分
        total_score = 0
        for factor, score in scores.items():
            total_score += score * self.weights[factor]

        scores["total_score"] = round(total_score, 2)
        return scores

    def _calculate_author_reputation(self, skill_metadata: Dict) -> float:
        """
        计算作者声誉评分

        Args:
            skill_metadata: 技能元数据字典

        Returns:
            作者声誉评分 (0-100)
        """
        author = skill_metadata.get("author", "unknown")

        # 这里可以集成实际的作者声誉系统
        # 暂时基于作者名称进行简单评分
        if author == "unknown":
            return 50
        elif author in ["verified", "trusted"]:
            return 90
        else:
            # 假设知名作者的评分较高
            return 70

    def _calculate_community_audit(self, skill_metadata: Dict) -> float:
        """
        计算社区审计评分

        Args:
            skill_metadata: 技能元数据字典

        Returns:
            社区审计评分 (0-100)
        """
        trust_chain = skill_metadata.get("trust_chain", [])

        # 基于信任链的长度和质量计算评分
        if not trust_chain:
            return 40
        elif len(trust_chain) >= 3:
            return 90
        else:
            return 60 + len(trust_chain) * 10

    def _calculate_usage_history(self, skill_metadata: Dict) -> float:
        """
        计算使用历史评分

        Args:
            skill_metadata: 技能元数据字典

        Returns:
            使用历史评分 (0-100)
        """
        # 这里可以集成实际的使用统计系统
        # 暂时返回默认值
        # 在实际应用中，应基于技能的使用频率、时长等因素计算
        return 60

    def _calculate_permission_reasonableness(self, skill_metadata: Dict) -> float:
        """
        计算权限合理性评分

        Args:
            skill_metadata: 技能元数据字典

        Returns:
            权限合理性评分 (0-100)
        """
        permissions = skill_metadata.get("permissions", [])

        # 评估权限的合理性
        # 越少的权限通常意味着越高的安全性
        if not permissions:
            return 90
        elif len(permissions) <= 2:
            return 80
        elif len(permissions) <= 5:
            return 60
        else:
            return 40

    def _calculate_code_quality(self, skill_metadata: Dict) -> float:
        """
        计算代码质量评分

        Args:
            skill_metadata: 技能元数据字典

        Returns:
            代码质量评分 (0-100)
        """
        # 这里可以集成实际的代码质量分析工具
        # 暂时基于哈希值的存在性进行简单评分
        if skill_metadata.get("hash", ""):
            return 70
        else:
            return 40

    def get_trust_level(self, total_score: float) -> str:
        """
        根据总评分获取信任级别

        Args:
            total_score: 总评分

        Returns:
            信任级别字符串
        """
        if total_score >= 80:
            return "高信任"
        elif total_score >= 60:
            return "中信任"
        elif total_score >= 40:
            return "低信任"
        else:
            return "不可信"

    def calculate_batch_trust_scores(self, skills_metadata: List[Dict]) -> List[Dict]:
        """
        批量计算多个技能的信任评分

        Args:
            skills_metadata: 技能元数据列表

        Returns:
            包含各技能评分的列表
        """
        results = []
        for metadata in skills_metadata:
            scores = self.calculate_trust_score(metadata)
            trust_level = self.get_trust_level(scores["total_score"])
            result = {
                "skill_name": metadata.get("name"),
                "scores": scores,
                "trust_level": trust_level
            }
            results.append(result)
        return results