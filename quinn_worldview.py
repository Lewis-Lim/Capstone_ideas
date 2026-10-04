from dataclasses import dataclass, field
from typing import Dict, List, Set


@dataclass
class BeliefNode:
    name: str
    depth: int  # 1 = Sensory periphery (brittle), 5 = Formal logic/math (bedrock)
    entrenched_value: float  # Epistemic inertia (0.0 to 1.0)
    bound_entities: Set[str] = field(
        default_factory=set
    )  # "Values of a variable"
    active: bool = True


class QuineanWebOfBelief:
    """Simulates Quine's Confirmation Holism and Ontological Commitment:

    1. 'To be is to be the value of a variable' -> Ontological commitment.
    2. Recalcitrant experience stresses the periphery first; core logic
       is revised only under extreme systemic pressure (Principle of Minimum Mutilation).
    """

    def __init__(self):
        self.web: Dict[str, BeliefNode] = {}

    def add_belief(
        self,
        name: str,
        depth: int,
        entrenched_value: float,
        bound_entities: Set[str],
    ):
        self.web[name] = BeliefNode(
            name, depth, entrenched_value, bound_entities
        )

    def encounter_recalcitrant_experience(
        self, target_domain: str, severity: float
    ) -> List[str]:
        """When empirical evidence contradicts the web, the system adjusts beliefs

        following the 'Principle of Minimum Mutilation' (protecting logic/math).
        """
        log = [
            f"⚡ Recalcitrant observation encountered in domain: '{target_domain}' (Severity: {severity})"
        ]

        # Candidates sorted by entrenchment (shallow/peripheral nodes are abandoned first)
        candidates = sorted(
            [b for b in self.web.values() if b.active],
            key=lambda x: (x.depth, x.entrenched_value),
        )

        for belief in candidates:
            # If observational stress exceeds inertia, abandon/revise this node
            threshold = belief.entrenched_value * (belief.depth / 2.0)
            if severity >= threshold:
                belief.active = False
                log.append(
                    f"  -> Discarded peripheral hypothesis: [{belief.name}] (Depth: {belief.depth})"
                )
                log.append(
                    f"     Core preserved via Principle of Minimum Mutilation."
                )
                return log

        # In extreme scenarios, even logic or spacetime frameworks are stressed
        deepest = candidates[-1]
        deepest.active = False
        log.append(
            f"  -> PARADIGM SHIFT: Deeply entrenched node revised: [{deepest.name}]"
        )
        return log

    def derive_ontological_commitments(self) -> Set[str]:
        """Quine's Criterion: 'To be is to be the value of a variable.'

        Ontology equals the union of entities quantified over in active theories.
        """
        commitments = set()
        for belief in self.web.values():
            if belief.active:
                commitments.update(belief.bound_entities)
        return commitments


# --- Running the Quinean Metaphysics Simulation ---
if __name__ == "__main__":
    web = QuineanWebOfBelief()

    # Deep interior: Formal logic and mathematics
    web.add_belief(
        name="Law of Non-Contradiction",
        depth=5,
        entrenched_value=0.99,
        bound_entities={"Logical Truth-Values"},
    )
    web.add_belief(
        name="Zermelo-Fraenkel Set Theory",
        depth=5,
        entrenched_value=0.95,
        bound_entities={"Abstract Sets", "Numbers"},
    )

    # Intermediate core: Fundamental physical theories
    web.add_belief(
        name="General Relativity & Quantum Mechanics",
        depth=3,
        entrenched_value=0.80,
        bound_entities={"Spacetime Manifold", "Quarks", "Photons"},
    )

    # Periphery: Observational hypothesis / empirical measurement
    web.add_belief(
        name="Classical Newtonian Velocity Addition at C",
        depth=1,
        entrenched_value=0.30,
        bound_entities={"Absolute Time", "Luminiferous Aether"},
    )

    print("=== INITIAL QUINEAN ONTOLOGICAL COMMITMENTS ===")
    print("Entities our worldview claims *actually exist*:")
    for entity in sorted(web.derive_ontological_commitments()):
        print(f"  • {entity}")

    print("\n=== STIMULATING THE WEB (Michelson-Morley Experiment) ===")
    events = web.encounter_recalcitrant_experience(
        target_domain="Speed of Light Invariance", severity=0.65
    )
    for line in events:
        print(line)

    print("\n=== REVISED ONTOLOGY AFTER SYSTEMIC UPDATE ===")
    print("Entities retained in our revised scientific ontology:")
    for entity in sorted(web.derive_ontological_commitments()):
        print(f"  • {entity}")