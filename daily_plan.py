import sys
from datetime import date

def run_daily_plan_check():
    print("=" * 60)
    print(f" DAILY PLANNER & CONTINGENCY CHECK | {date.today().strftime('%B %d, %Y')}")
    print("=" * 60)
    
    # 1. Main Goal
    plan_a = input("\n1. [PLAN A] What is the primary task/goal for today?\n> ").strip()
    if not plan_a:
        print("No plan entered. Exiting check.")
        return

    # 2. Early Warning Indicators & Prevention
    print("\n2. [PREVENTION & SIGNS] Think ahead:")
    signs = input("   What are the early signs that Plan A is slipping or off-track?\n> ").strip()
    prevention = input("   What proactive steps will you take NOW to prevent those friction points?\n> ").strip()

    # 3. Remedial / Mid-Course Adjustments
    print("\n3. [REMEDIAL ACTION / PLAN B] Mid-course adjustment:")
    plan_b = input("   If warning signs appear, what immediate pivot will you make?\n> ").strip()

    # 4. Secondary Contingency / Plan C
    print("\n4. [HARD BACKUP / PLAN C] Worst-case contingency:")
    plan_c = input("   If Plan A completely fails, what is the fallback option to secure an outcome?\n> ").strip()

    # 5. Communication / Escalation
    print("\n5. [COMMUNICATION] Stakeholder update:")
    share = input("   Who needs to be kept in the loop early if indicators turn negative?\n> ").strip()

    # Summary Output
    print("\n" + "=" * 60)
    print(" EXECUTION & RISK PROFILE SUMMARY")
    print("=" * 60)
    print(f"• Primary Goal (Plan A) : {plan_a}")
    print(f"• Early Risk Indicators : {signs if signs else 'None specified'}")
    print(f"• Preventive Actions   : {prevention if prevention else 'None specified'}")
    print(f"• Remedial Plan B      : {plan_b if plan_b else 'None specified'}")
    print(f"• Fallback Plan C      : {plan_c if plan_c else 'None specified'}")
    print(f"• Escalation / Update  : {share if share else 'None specified'}")
    print("=" * 60)
    print("Check complete. Focus on execution and keep monitoring early signs!\n")

if __name__ == "__main__":
    run_daily_plan_check()