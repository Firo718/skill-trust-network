# Skill Trust Network

基于@eudaemon_0在Moltbook上提出的**Isnad Chains**（传承链）概念，构建的AI技能安全审计和信任评分系统。

![Skill Trust Network](https://img.shields.io/badge/version-1.0.0-blue) ![License](https://img.shields.io/badge/license-MIT-green)

## 🎯 核心功能

### 🔒 安全审计
- **技能元数据收集**：自动扫描技能的作者、权限、版本等信息
- **多维度信任评分**：作者声誉、社区审计、使用历史、权限合理性、代码质量
- **安全风险评估**：识别潜在的安全威胁和权限滥用

### 🔗 Isnad Chains（传承链）
- **审计记录链**：每次技能审计都会添加到传承链中
- **信任验证**：验证技能的历史审计记录和社区评价
- **声誉追踪**：跟踪技能在整个AI社区中的信任度变化

### 📊 Moltbot集成
- **安全仪表板**：实时监控所有已安装技能的安全状态
- **自动化警报**：发现高风险技能时自动通知
- **合规检查**：确保技能符合最低安全标准

## 🚀 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 基本使用
```python
from skill_trust_network import SkillTrustNetwork

# 初始化技能信任网络
stn = SkillTrustNetwork()

# 审计单个技能
report = stn.audit_skill("weather")
print(report)

# 审计所有技能
all_reports = stn.audit_all_skills()
print(all_reports)

# 获取安全仪表板数据
dashboard = stn.get_security_dashboard_data()
print(dashboard)
```

### 高级功能：Isnad Chains
```python
# 添加审计记录到传承链
skill_hash = "your_skill_hash"
audit_result = {"total_score": 85, "security_issues": []}
stn.add_audit_to_chain(skill_hash, "your_agent_name", audit_result)

# 验证传承链
verification = stn.verify_isnad_chain(skill_hash)
print(verification)
```

## 📁 项目结构

```
skill_trust_network/
├── README.md
├── requirements.txt
├── setup.py
├── skill_trust_network/
│   ├── __init__.py
│   ├── modules/
│   │   ├── metadata_collector.py
│   │   ├── trust_scoring.py
│   │   ├── security_audit.py
│   │   └── isnad_chain.py
│   └── integration/
│       └── moltbot_integration.py
├── examples/
│   ├── basic_usage.py
│   └── isnad_chains_demo.py
├── tests/
│   └── test_skill_trust_network.py
└── docs/
    └── API文档.md
```

## 💡 设计理念

### 基于@eudaemon_0的Isnad Chains概念
> "技能文件是未签名的二进制文件...我们需要技能签名、Isnad chains（传承链）、权限清单和社区审计。"

我们的实现完全遵循这一安全理念，为AI技能生态系统提供可信的安全基础设施。

### 三层安全架构
1. **预防层**：安装前安全检查
2. **检测层**：运行时安全监控  
3. **响应层**：风险技能自动隔离

## 🤝 贡献指南

欢迎贡献！请遵循以下步骤：

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

## 📜 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🙏 致谢

- **@eudaemon_0** - Isnad Chains概念的提出者
- **Moltbook社区** - AI安全讨论的启发
- **所有贡献者** - 让这个项目变得更好

---

**Build a secure, verifiable AI skill ecosystem together!** 🦞