#!/usr/bin/env python3
"""
Isnad Chain (传承链) 验证模块
基于@eudaemon_0提出的概念，实现技能的传承链验证
"""

import hashlib
import json
from datetime import datetime
from typing import Dict, List, Optional

class IsnadChain:
    """技能传承链验证类"""
    
    def __init__(self):
        self.chain_file = "/home/admin/clawd/skill_trust_network/data/isnad_chains.json"
        self.load_chains()
    
    def load_chains(self):
        """加载现有的传承链数据"""
        try:
            with open(self.chain_file, 'r', encoding='utf-8') as f:
                self.chains = json.load(f)
        except FileNotFoundError:
            self.chains = {}
            self.save_chains()
    
    def save_chains(self):
        """保存传承链数据"""
        # 确保目录存在
        import os
        os.makedirs(os.path.dirname(self.chain_file), exist_ok=True)
        
        with open(self.chain_file, 'w', encoding='utf-8') as f:
            json.dump(self.chains, f, indent=2, ensure_ascii=False)
    
    def create_skill_hash(self, skill_metadata: Dict) -> str:
        """为技能创建唯一哈希值"""
        # 使用技能的关键信息创建哈希
        hash_input = f"{skill_metadata.get('name', '')}:{skill_metadata.get('version', '')}:{skill_metadata.get('author', '')}"
        return hashlib.sha256(hash_input.encode()).hexdigest()
    
    def add_audit_to_chain(self, skill_hash: str, auditor: str, audit_result: Dict) -> bool:
        """向传承链添加审计记录"""
        if skill_hash not in self.chains:
            self.chains[skill_hash] = {
                "skill_hash": skill_hash,
                "created_at": datetime.now().isoformat(),
                "audit_chain": []
            }
        
        audit_record = {
            "auditor": auditor,
            "timestamp": datetime.now().isoformat(),
            "result": audit_result,
            "trust_score": audit_result.get("total_score", 0)
        }
        
        self.chains[skill_hash]["audit_chain"].append(audit_record)
        self.save_chains()
        return True
    
    def verify_isnad_chain(self, skill_hash: str) -> Dict:
        """验证技能的传承链"""
        if skill_hash not in self.chains:
            return {
                "verified": False,
                "message": "未找到该技能的传承链记录",
                "chain_length": 0,
                "average_trust_score": 0,
                "auditors": []
            }
        
        chain = self.chains[skill_hash]
        audit_chain = chain["audit_chain"]
        
        if not audit_chain:
            return {
                "verified": False,
                "message": "传承链为空",
                "chain_length": 0,
                "average_trust_score": 0,
                "auditors": []
            }
        
        # 计算平均信任评分
        total_score = sum(record["trust_score"] for record in audit_chain)
        avg_score = total_score / len(audit_chain)
        
        # 获取审计员列表
        auditors = [record["auditor"] for record in audit_chain]
        
        return {
            "verified": True,
            "message": f"传承链验证成功，包含{len(audit_chain)}次审计记录",
            "chain_length": len(audit_chain),
            "average_trust_score": round(avg_score, 2),
            "auditors": auditors,
            "latest_audit": audit_chain[-1]["timestamp"]
        }
    
    def get_skill_reputation(self, skill_name: str) -> Dict:
        """获取技能的整体声誉评分"""
        # 这里需要遍历所有技能找到匹配的
        # 简化版本：返回基于传承链的声誉
        reputation_data = {
            "skill_name": skill_name,
            "isnad_verified": False,
            "community_trust": 0,
            "audit_count": 0,
            "risk_level": "未知"
        }
        
        # 在实际实现中，这里会查询具体的技能哈希
        return reputation_data

def main():
    """测试IsnadChain功能"""
    isnad = IsnadChain()
    
    # 测试数据
    test_skill = {
        "name": "weather",
        "version": "1.0.0", 
        "author": "trusted_author"
    }
    
    skill_hash = isnad.create_skill_hash(test_skill)
    print(f"技能哈希: {skill_hash}")
    
    # 添加审计记录
    test_audit = {
        "total_score": 85,
        "security_issues": [],
        "compliance_status": True
    }
    
    isnad.add_audit_to_chain(skill_hash, "xiaomi_cat", test_audit)
    print("审计记录已添加到传承链")
    
    # 验证传承链
    verification = isnad.verify_isnad_chain(skill_hash)
    print(f"传承链验证结果: {verification}")

if __name__ == "__main__":
    main()