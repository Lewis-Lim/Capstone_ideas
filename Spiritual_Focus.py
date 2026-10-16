import datetime

class SpiritualFocusTracker:
    def __init__(self):
        self.pillars = {
            "Kingdom Mission": "Seeking God's kingdom and righteousness first in daily choices.",
            "Divine Wisdom": "Pursuing discernment, understanding, and truth over worldly foolishness.",
            "Long-Term Stability": "Building a life on the rock of faith, character, and integrity.",
            "Diligence & Purpose": "Working with excellence as unto the Lord, not for temporary wealth."
        }

    def display_manifesto(self):
        print("=" * 65)
        print("    DAILY COMMITMENT: WORKING FOR GOD, JESUS, AND THE HOLY SPIRIT")
        print("=" * 65)
        print("Scriptural Grounding:")
        print(" 'Work willingly at whatever you do, as though you were working")
        print("  for the Lord rather than for people.' — Colossians 3:23\n")
        
        print("Core Pillars of Focus:")
        for pillar, description in self.pillars.items():
            print(f" • {pillar.upper()}: {description}")
        print("=" * 65)

    def daily_check_in(self):
        today = datetime.date.today().strftime("%A, %B %d, %Y")
        print(f"\n[ Daily Reflection for {today} ]\n")
        
        q1 = input("1. Did your actions today align with eternal purpose rather than material gain? (yes/no): ")
        q2 = input("2. In what area did you seek Godly wisdom or discernment today?: ")
        q3 = input("3. What intentional work did you do to build spiritual stability and character?: ")

        print("\n" + "-" * 65)
        print("SUMMARY & PRAYER FOCUS:")
        print("-" * 65)
        
        if q1.strip().lower() == 'yes':
            print("✓ Keeping your eyes fixed on Christ and the eternal perspective.")
        else:
            print("! Re-center your heart tomorrow. Remember that material wealth fades, but eternal fruit remains.")
            
        print(f"• Wisdom focus today: {q2}")
        print(f"• Foundation built today: {q3}")
        print("\nEncouragement:")
        print(" Continue to labor diligently with the guidance of the Holy Spirit.")
        print(" True stability and riches are found in Christ alone.\n")

if __name__ == "__main__":
    tracker = SpiritualFocusTracker()
    tracker.display_manifesto()
    tracker.daily_check_in()