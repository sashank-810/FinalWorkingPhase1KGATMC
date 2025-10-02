import litellm
import streamlit as st

class TokenTracker:
    def __init__(self):
        self.reset()

    def reset(self):
        self._total_prompt_tokens = 0
        self._total_completion_tokens = 0
        self._total_cost = 0.0
        self._calls = 0

    def add_usage(self, response):
        if response and hasattr(response, 'usage'):
            usage = response.usage
            prompt_tokens = usage.prompt_tokens or 0
            completion_tokens = usage.completion_tokens or 0
            
            self._total_prompt_tokens += prompt_tokens
            self._total_completion_tokens += completion_tokens
            self._calls += 1
            
            try:
                cost = litellm.completion_cost(completion_response=response)
                self._total_cost += cost if cost is not None else 0.0
            except Exception:
                pass

    def display(self):
        """Displays the token usage metrics in the Streamlit sidebar."""
        total_tokens = self._total_prompt_tokens + self._total_completion_tokens
        
        with st.sidebar:
            st.markdown("---")
            st.subheader("📊 Run Metrics")
            col1, col2 = st.columns(2)
            col1.metric("API Calls", f"{self._calls}")
            col2.metric("Total Tokens", f"{total_tokens}")
            st.info(f"**Estimated Cost:** ${self._total_cost:.6f}")


# Global instance to be used by the callback
token_tracker = TokenTracker()

# Callback function to register with litellm
def track_token_usage_callback(kwargs):
    """LiteLLM callback function to track token usage and cost."""
    response_obj = kwargs.get("response_obj")
    if response_obj:
        token_tracker.add_usage(response_obj)