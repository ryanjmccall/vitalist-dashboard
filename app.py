import streamlit as st
import plotly.graph_objects as go

# --- 1. PAGE CONFIG & STYLING (Clean Light Theme) ---
st.set_page_config(
    page_title="Vitalism Impact Monitor",
    page_icon="⚕️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# FORCE LIGHT THEME & CUSTOM STYLING
st.markdown("""
    <style>
    /* Main Background - Clean White */
    .stApp {
        background-color: #ffffff;
        color: #111827; /* Slate 900 */
        font-family: 'Inter', sans-serif;
    }
    
    /* Card Styling - Soft Gray with Subtle Borders */
    .metric-card {
        background-color: #f9fafb; /* Gray 50 */
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #e5e7eb; /* Gray 200 */
        text-align: left;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05);
        margin-bottom: 16px;
    }
    
    /* Typography */
    .big-number {
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: -0.02em;
        line-height: 1.2;
    }
    .label {
        font-size: 0.875rem;
        color: #6b7280; /* Gray 500 */
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 8px;
    }
    .sub-text {
        font-size: 0.8rem;
        color: #9ca3af;
        margin-top: 4px;
    }
    
    /* Specific Color Accents */
    .accent-human { color: #0284c7; } /* Sky Blue */
    .accent-dog { color: #0d9488; }   /* Teal */
    .accent-alert { color: #dc2626; } /* Red 600 */
    .accent-good { color: #059669; }  /* Emerald 600 */
    
    /* Remove Streamlit default margin garbage */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 5rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. HEADER ---
st.title("Longevity Funding Gap")
st.markdown("### The disparity between the scale of aging and our investment in solving it.")
st.markdown("---")

# --- 3. THE "STAKES" (People & Dogs) ---
# This mimics the "Impact" section from the HTML file
col_humans, col_dogs = st.columns(2)

with col_humans:
    st.markdown("""
        <div class="metric-card">
            <div class="label">Affected Population (Humans)</div>
            <div class="big-number accent-human">8.2 Billion</div>
            <div class="sub-text">Source: UN World Population Prospects (2025)</div>
        </div>
    """, unsafe_allow_html=True)

with col_dogs:
    st.markdown("""
        <div class="metric-card">
            <div class="label">Affected Population (Dogs)</div>
            <div class="big-number accent-dog">900 Million</div>
            <div class="sub-text">Source: Global Pet Industry Est. (2025)</div>
        </div>
    """, unsafe_allow_html=True)

# --- 4. DATA & INTERACTIVITY ---
# Hardcoded 2025 Estimates
GLOBAL_GDP_TRIL = 117.2
ACTUAL_FUNDING_BIL = 3.2

# Slider for "Target"
st.markdown("#### Adjust Target Commitment")
target_pct = st.slider("Percentage of Global GDP", 0.1, 5.0, 1.0, 0.1, label_visibility="collapsed")
st.caption(f"Current Target: **{target_pct}%** of Global GDP")

# Calculations
target_funding_bil = (GLOBAL_GDP_TRIL * 1000) * (target_pct / 100)
shortfall_factor = target_funding_bil / ACTUAL_FUNDING_BIL

# --- 5. FINANCIAL METRICS GRID ---
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="label">Target Goal ({target_pct}%)</div>
            <div class="big-number accent-good">${int(target_funding_bil):,}B</div>
            <div class="sub-text">What we should spend</div>
        </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="label">Actual Funding</div>
            <div class="big-number" style="color: #d97706;">${ACTUAL_FUNDING_BIL}B</div>
            <div class="sub-text">Public + Private (2025)</div>
        </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
        <div class="metric-card" style="border-color: #fecaca; background-color: #fef2f2;">
            <div class="label" style="color: #dc2626;">The Shortfall</div>
            <div class="big-number accent-alert">{int(shortfall_factor)}x</div>
            <div class="sub-text" style="color: #ef4444;">Underfunded Magnitude</div>
        </div>
    """, unsafe_allow_html=True)

# --- 6. CHARTS (Light Theme Adapted) ---
st.markdown("### Visualization")

# Chart 1: The Gap (Log Scale)
fig_gap = go.Figure()
fig_gap.add_trace(go.Bar(
    x=['Actual Funding', 'Target Funding'],
    y=[ACTUAL_FUNDING_BIL, target_funding_bil],
    marker_color=['#d97706', '#059669'], # Gold, Emerald
    text=[f"${ACTUAL_FUNDING_BIL}B", f"${int(target_funding_bil):,}B"],
    textposition='auto',
))

fig_gap.update_layout(
    title="Funding Gap (Logarithmic Scale)",
    yaxis_type="log",
    yaxis_title="Billions USD (Log Scale)",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    font=dict(color='#374151'), # Gray 700
    margin=dict(t=30, b=0, l=0, r=0),
    height=300
)
st.plotly_chart(fig_gap, use_container_width=True)

# --- 7. FOOTER CTA ---
st.divider()
st.markdown(f"""
    <div style="text-align: center; padding: 20px;">
        <p style="font-size: 1.1rem; color: #374151; margin-bottom: 20px;">
            For <strong>8.2 billion people</strong> and <strong>900 million dogs</strong>, 
            we are underfunding the solution by <strong>{int(shortfall_factor)}x</strong>.
        </p>
        <a href="https://www.vitalism.io" target="_blank" style="
            background-color: #ea580c; 
            color: white; 
            padding: 12px 32px; 
            border-radius: 6px; 
            text-decoration: none; 
            font-weight: bold; 
            font-size: 1rem;
            box-shadow: 0 4px 6px -1px rgba(234, 88, 12, 0.4);">
            Join the Vitalism Movement &rarr;
        </a>
    </div>
""", unsafe_allow_html=True)
