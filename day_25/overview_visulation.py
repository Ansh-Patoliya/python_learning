# Data Visualization Overview (Matplotlib) — Comments Only, Short & Simple
# Audience: Beginners/Intermediate. Goal: Quick mental model and best practices.

# What & Why
# - Visualize data to see trends, compare groups, spot outliers, and explain results.
# - Matplotlib = core Python plotting library; flexible, reliable, widely used.

# Core Concepts
# - Figure: full canvas; Axes: one plot area inside a Figure.
# - Artist: any drawable element (lines, bars, text, legend, etc.).
# - Backends: renderers (Agg for files, GUI for interactive).

# Two APIs
# - Pyplot (stateful): quick demos.
# - Object-Oriented (OO): fig/ax objects; clearer, scalable; prefer for real work.

# Common Charts (when to use)
# - Line: trend over ordered x (often time).
# - Scatter: relationship between two variables (add color/size for more dims).
# - Bar/Barh: compare categories (sort meaningfully; show error bars if needed).
# - Histogram/KDE: distribution shape; choose bins; KDE smooths.
# - Box/Violin: compare distributions across groups.
# - Heatmap/Imshow: 2D matrix fields; always add a colorbar.
# - Hexbin/2D hist: dense scatter alternatives.

# Axes & Scales
# - Set limits honestly; pick linear/log/symlog to match data.
# - Ticks: readable locations; format numbers/dates.
# - Aspect ratio: match data meaning (e.g., square for distances).

# Labels, Titles, Legends, Annotations
# - Always label axes with units; concise title/subtitle.
# - Legends: don’t cover data; consider direct labels.
# - Annotations: short callouts to highlight key points.

# Color & Style
# - Use perceptual, colorblind-friendly palettes.
# - Sequential for magnitude (e.g., viridis), diverging around a midpoint, qualitative for categories.
# - Keep contrast high; use consistent fonts/sizes; prefer simple themes.

# Layouts
# - Subplots for comparisons (small multiples > cluttered single plot).
# - Shared axes for comparable scales; use tight/constrained layout to avoid overlap.

# Time Series & Categories
# - Parse dates; sensible tick spacing/rotation.
# - Sort categories by value or logical order; horizontal bars for long labels.

# Performance & Export
# - Downsample/aggregate; use rasterization for huge point sets.
# - Export with correct size/DPI; PNG (raster), SVG/PDF (vector); include fonts.

# Best Practices
# - Clarity first: minimal non-data ink; readable text; show units and sources.
# - Avoid 3D and pie charts for precise comparisons; prefer bars/lines.
# - Be consistent with colors/labels across figures.

# Quick Guide
# - Trend → Line; Comparison → Bar; Relation → Scatter/Hexbin; Distribution → Hist/KDE/Box; Matrix → Heatmap.


