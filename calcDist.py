import math
import numpy as np

rayon = 6371
lat1 = 48.8534951
lat2 = 51.5073219
long1 = 2.3483915
long2= -.1276474

phi1 = np.radians(lat1)
print(phi1)
phi2 = np.radians(lat2)
print(phi2)
delta_phi = np.radians(lat2-lat1)
print(delta_phi)
delta_lambda = np.radians(long2-long1)
print(delta_lambda)
a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2)**2
print(a)
res = rayon * (2* np.arctan2(np.sqrt(a),  np.sqrt(1-a)))
print(res)
print('la distance entre Londres et Paris est: ', np.round(res,2), 'kms')