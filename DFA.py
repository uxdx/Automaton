from typing import Dict, List


class DFA:
    """DFA(Deterministic Finite Automaton)
    有限個の状態数を持つ決定性オートマトン
    """

    def __init__(self, states: List[str], symbols: List[str], functions: Dict[tuple[str, str], str], initialState: str, acceptingState: List[str]) -> None:
        """Constructor

        Args:
            states (List[str]): 状態の有限集合Q
            symbols (List[str]): 入力記号の有限集合Σ
            functions (Dict[tuple[str, str], str]): 動作関数δ(Q X Σ -> Q)
            initialState (str): 初期状態 q0 ∈ Q
            acceptingState (List[str]): 受理状態の有限集合 F ⊆ Q
        """
        self.states = states
        self.symbols = symbols
        self.functions = functions
        self.initialState = initialState
        self.acceptingState = acceptingState

    def execute(self, language: str) -> bool:
        """入力記号列（言語）に対しオートマトンを動かす。

        Args:
            language (str): 入力記号列（言語）

        Returns:
            bool: 入力された言語が受理する場合Trueを返す
        """
        currentState = self.initialState

        for w in [*language]:
            try:
                result = self.functions[(currentState, w)]
            except KeyError:
                # 転移先が定義されていない場合、Falseを返す
                return False

            print("(", currentState, ", ", w, ") |- ", result)
            currentState = result

        # 動作が終わった時点で状態が受理状態集合に入っているか判別
        if acceptingState.__contains__(currentState):
            return True
        return False


if __name__ == "__main__":
    # Test Codes
    states = ["q0", "q1"]
    symbols = ["a", "b"]
    initialState = "q0"
    acceptingState = "q1"

    f = {
        ("q0", "a"): "q1",
        ("q0", "b"): "q0",
        ("q1", "a"): "q1",
        ("q1", "b"): "q0",
    }
    # DFA構成
    dfa = DFA(states=states, symbols=symbols, functions=f,
              initialState=initialState, acceptingState=acceptingState)
    # 実行
    if dfa.execute("aabaa"):
        print("Succeed")
    else:
        print("Failed")
