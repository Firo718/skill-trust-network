#!/usr/bin/env python3
"""
Basic usage example for Skill Trust Network
"""

from skill_trust_network import SkillTrustNetwork

def main():
    # Initialize the trust network
    stn = SkillTrustNetwork()
    
    # Audit a specific skill
    skill_name = "weather"
    report = stn.audit_skill(skill_name)
    
    print(f"Security audit report for {skill_name}:")
    print(f"Risk level: {report['security_assessment']['risk_level']}")
    print(f"Trust score: {report['trust_scores']['total_score']}")
    print(f"Compliance: {report['compliance_status']['overall_compliance']}")
    
    # Audit all skills
    all_reports = stn.audit_all_skills()
    print(f"\nTotal skills audited: {all_reports['summary']['total_skills']}")
    print(f"Average trust score: {all_reports['summary']['average_trust_score']}")

if __name__ == "__main__":
    main()