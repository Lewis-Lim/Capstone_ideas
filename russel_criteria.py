from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class IdeologicalClaim:
    name: str
    is_falsifiable: bool
    empirical_evidence_weight: float  # Scale 0.0 (pure assertion) to 1.0 (reproducible data)
    degree_of_conviction: float  # Scale 0.0 (provisional hypothesis) to 1.0 (absolute certainty)
    welcomes_dissent: bool
    appeals_to_fear_or_passion: bool
    withstands_expert_consensus_doubt: bool


class RussellEpistemicAuditor:
    """Evaluates systems of thought based on Bertrand Russell's criteria

    for rational belief, intellectual honesty, and skepticism.
    """

    @staticmethod
    def audit(claim: IdeologicalClaim) -> Tuple[float, List[str]]:
        score = 0.0
        max_score = 100.0
        critiques = []

        # 1. Proportionality of Belief to Evidence (Russell's Core Axiom)
        # "Give to any hypothesis that is worth your consideration only that degree
        # of credence which the evidence warrants."
        epistemic_balance = (
            claim.empirical_evidence_weight - claim.degree_of_conviction
        )
        if epistemic_balance >= 0:
            score += 25
            critiques.append(
                "✓ Proportionality met: Conviction does not outrun evidence."
            )
        else:
            deficit = abs(epistemic_balance) * 25
            critiques.append(
                f"✗ Fanaticism warning: Conviction exceeds empirical warrant by {abs(epistemic_balance):.2f}."
            )
            score += max(0.0, 25 - deficit)

        # 2. Intellectual Fallibility & Openness to Refutation
        # "Do not feel absolutely certain of anything."
        if claim.is_falsifiable and claim.degree_of_conviction < 1.0:
            score += 25
            critiques.append(
                "✓ Fallibilism preserved: Admits possibility of error."
            )
        else:
            critiques.append(
                "✗ Dogmatism detected: Absolute certainty claimed; lacks falsifiability criteria."
            )

        # 3. Attitude Toward Dissent and Authority
        # "Have no respect for the authority of others, for there are always contrary
        # authorities to be found." / "Do not fear being eccentric in opinion."
        if claim.welcomes_dissent:
            score += 25
            critiques.append(
                "✓ Intellectual liberty: Welcomes contrary arguments and scrutiny."
            )
        else:
            critiques.append(
                "✗ Authoritarian impulse: Suppresses or vilifies dissent."
            )

        # 4. Reason vs. Emotional Exploitation
        # Russell warned that opinions held with passion always signify lack of rational grounds.
        # "When there is evidence, no one speaks of 'faith'. We only speak of faith when we wish
        # to substitute emotion for evidence."
        if not claim.appeals_to_fear_or_passion:
            score += 15
            critiques.append(
                "✓ Dispassionate inquiry: Grounded in analysis rather than emotional coercion."
            )
        else:
            critiques.append(
                "✗ Emotional bias: Leverages passion, fear, or tribal loyalty over reason."
            )

        # 5. Respect for Genuine Scepticism & Expert Consensus
        # If the experts agree, the opposite cannot be held as certain.
        if claim.withstands_expert_consensus_doubt:
            score += 10
            critiques.append(
                "✓ Sceptical compliance: Respects limits where experts disagree or remain agnostic."
            )
        else:
            critiques.append(
                "✗ Premature certainty: Disregards legitimate expert doubts or methodological skepticism."
            )

        return score, critiques

    @staticmethod
    def classify_ideology(score: float) -> str:
        if score >= 80:
            return "Rational Epistemic Framework (Russellian Free-Inquiry)"
        elif score >= 50:
            return "Mixed Ideological System (Prone to Unverified Assumptions)"
        else:
            return "Dogmatic / Fanatical Ideology (Violates Russell's Ethics of Belief)"


# --- Demonstration of Russell's Criteria in Action ---
if __name__ == "__main__":
    systems = [
        IdeologicalClaim(
            name="Dogmatic Totalitarianism / Religious Fundamentalism",
            is_falsifiable=False,
            empirical_evidence_weight=0.15,
            degree_of_conviction=1.0,  # Absolute certainty
            welcomes_dissent=False,
            appeals_to_fear_or_passion=True,
            withstands_expert_consensus_doubt=False,
        ),
        IdeologicalClaim(
            name="Scientific Skepticism / Russellian Empiricism",
            is_falsifiable=True,
            empirical_evidence_weight=0.85,
            degree_of_conviction=0.80,  # Proportionate, provisional credence
            welcomes_dissent=True,
            appeals_to_fear_or_passion=False,
            withstands_expert_consensus_doubt=True,
        ),
    ]

    for sys in systems:
        print(f"\n{'='*60}")
        print(f"AUDITING: {sys.name}")
        print(f"{'='*60}")
        score, feedback = RussellEpistemicAuditor.audit(sys)
        for line in feedback:
            print(f"  {line}")
        print(f"\nFinal Rationality Index: {score:.1f}/100")
        print(f"Verdict: {RussellEpistemicAuditor.classify_ideology(score)}")