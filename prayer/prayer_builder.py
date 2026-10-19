"""
Reformed Prayer Builder
-----------------------
This script helps you structure and write detailed Reformed Christian prayers 
by guiding you through key theological components:
1. Adoration (Praising God's sovereignty, holiness, and attributes)
2. Confession (Acknowledging sin and relying on Christ's mediation)
3. Thanksgiving (Recognizing God's providence and redemption)
4. Petition & Intercession (Lifting up personal and communal needs grounded in Scripture)
5. Conclusion (Doxology and praying in Christ's name)
"""

def generate_reformed_prayer():
    print("=" * 50)
    print("          REFORMED PRAYER BUILDER          ")
    print("=" * 50 + "\n")
    print("This tool will guide you step-by-step to craft a rich, detailed, and Scripture-aligned prayer.\n")

    # 1. Adoration
    print("--- Step 1: Adoration & Invocation ---")
    print("Focus on God's character, holiness, sovereignty, and covenant faithfulness.")
    attributes = input("What attributes or works of God are you praising Him for today? (e.g., His sovereign grace, mercy, holiness): ")
    scripture_adoration = input("Any specific Bible verse or passage that inspires this praise? (optional): ")

    # 2. Confession
    print("\n--- Step 2: Confession & Repentance ---")
    print("Acknowledge your shortcomings honestly, anchoring your hope entirely in Christ's finished work.")
    sin_confessed = input("What specific sins, failures, or struggles are you bringing before the Lord?: ")
    reliance = input("How are you leaning on Christ's righteousness and mediation here?: ")

    # 3. Thanksgiving
    print("\n--- Step 3: Thanksgiving ---")
    print("Give thanks for God's temporal providence and spiritual blessings in redemption.")
    providence = input("What temporal or spiritual blessings are you thanking God for today?: ")

    # 4. Petition & Intercession
    print("\n--- Step 4: Petition & Intercession ---")
    print("Present your requests for yourself, the church, and the world, submitting to His wise will.")
    personal_needs = input("What personal needs or spiritual growth areas are you praying for?: ")
    intercession = input("Who else are you lifting up (family, church, leaders, the lost)?: ")

    # 5. Conclusion
    print("\n--- Step 5: Conclusion & Doxology ---")
    doxology = input("How would you like to praise God as you close? (e.g., 'For Yours is the kingdom...'): ")

    # Compile the prayer output
    print("\n" + "=" * 50)
    print("          YOUR STRUCTURED PRAYER          ")
    print("=" * 50 + "\n")

    print("Heavenly Father, Sovereign Lord,\n")
    
    if attributes.strip():
        print(f"We come before Your glorious presence to adore You. {attributes}.")
        if scripture_adoration.strip():
            print(f"As Your Word reminds us in {scripture_adoration}, You alone are worthy of all honor and praise.")
    else:
        print("We come before Your glorious presence to adore Your holy, sovereign, and covenant-keeping name.")

    print("\nLord, in the light of Your absolute holiness, we confess our sin and brokenness.")
    if sin_confessed.strip():
        print(f"We acknowledge that we have fallen short of Your glory: {sin_confessed}.")
    if reliance.strip():
        print(f"We look away from our own merits and rest wholly {reliance}.")
    else:
        print("We cast ourselves completely upon the finished work, righteousness, and intercession of Jesus Christ our Mediator.")

    print("\nFather, our hearts overflow with gratitude.")
    if providence.strip():
        print(f"We thank You for Your daily providence, sustaining grace, and spiritual blessings: {providence}.")
    else:
        print("We thank You for every spiritual blessing in heavenly places and Your faithful care over our lives.")

    print("\nAccording to Your perfect and wise will, we humbly ask:")
    if personal_needs.strip():
        print(f"- Grant us grace and steadfast faith in our personal walk: {personal_needs}.")
    if intercession.strip():
        print(f"- Pour out Your mercy, truth, and convicting power upon others: {intercession}.")

    print("\nWe offer these petitions trusting in Your sovereign goodness and loving-kindness.")
    
    if doxology.strip():
        print(f"{doxology}")
    else:
        print("For Yours is the kingdom, and the power, and the glory, forever and ever. Amen.")
    
    print("\n" + "=" * 50)

if __name__ == "__main__":
    generate_reformed_prayer()