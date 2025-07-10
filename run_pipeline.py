"""Example script demonstrating the data->analysis->decision workflow."""

from analysis.technical_analysis import TechnicalAnalysisNode
from decision.decision_synthesizer import DecisionSynthesizer


def main():
    node = TechnicalAnalysisNode()
    result = node.run("AAPL", period="1mo", interval="1d")
    if result is None:
        print("Failed to fetch data")
        return
    print("Technical indicators calculated.")
    decision = DecisionSynthesizer().synthesize(result)
    print(f"Decision: {decision}")


if __name__ == "__main__":
    main()
