# Auto-generated pipeline script (best effort).
# Edit file paths / connection strings as needed.
# Target dataset id: raw_cf5e1d1c

import pandas as pd

df = None

# Step 1: raw — bike_model_specs.csv (raw_cf5e1d1c)
#   schema_hash: 1126bc859f04fa24b0833a509b3164c105d760eaaad06fd034c16e6c4a94e5d6
#   fingerprint: 2a3f8fbeffacbb56e3bd1cf2a6ba6b8adb42acdc56c7a192ba88f0f93e24ac97
df = pd.read_csv('/Users/nkumar/ai-data-science-team/data/bike_model_specs.csv')

# Final output
print('Final shape:', getattr(df, 'shape', None))
# df.to_csv('final_dataset.csv', index=False)
