import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Simular uma grade topográfica digital (DEM) para a costa de Onerahi, Whangārei
np.random.seed(101)
grid_size = 100  # Matriz 100x100 representando uma área de 1km x 1km
x = np.linspace(0, 1000, grid_size)
y = np.linspace(0, 1000, grid_size)
X, Y = np.meshgrid(x, y)

# Criar uma inclinação topográfica simulada (da praia para o interior) com rugosidade natural
elevation = (X / 250) + np.random.normal(0, 0.15, (grid_size, grid_size))
# Garantir que a linha da maré baixa comece em 0 metros
elevation = np.clip(elevation, 0, None)

# 2. Definir os cenários de elevação do nível do mar (SLR) no horizonte de 2100 para NZ
current_high_tide = 1.2   # Maré alta astronômica atual em metros (MHWS)
slr_scenario_2100 = 1.0   # Projeção intermediária-alta de subida do nível do mar (1.0m)
storm_surge = 0.8         # Evento de tempestade extrema (1 em 50 anos)

total_flood_level = current_high_tide + slr_scenario_2100 + storm_surge

# 3. Análise Geoespacial de Inundação Masking
flooded_mask = elevation <= total_flood_level
flooded_area_pct = (np.sum(flooded_mask) / (grid_size * grid_size)) * 100

print(f"--- Relatório de Risco: Whangārei Harbour Baseline ---")
print(f"Nível Crítico de Inundação Projetado (MHW + SLR + Storm Surge): {total_flood_level:.2f} metros")
print(f"Área Total da Infraestrutura Costeira Vulnerável: {flooded_area_pct:.1f}%\n")

# 4. Gerar Mapa de Vulnerabilidade de Engenharia Costeira
plt.figure(figsize=(10, 8))
contour = plt.contourf(X, Y, elevation, levels=15, cmap='terrain')
cbar = plt.colorbar(contour)
cbar.set_label('Terrain Elevation (Meters above local sea level)', fontsize=10)

# Sobrepor a zona de inundação crítica em azul translúcido
plt.imshow(flooded_mask, extent=[0, 1000, 0, 1000], origin='lower', cmap='Blues', alpha=0.5, label='Zona de Inundação Crítica (2100)')

plt.title('Coastal Inundation & SLR Risk Map (2100) - Onerahi, Whangārei', fontsize=12, fontweight='bold', pad=15)
plt.xlabel('Distance from Coastline (Meters)', fontsize=10)
plt.ylabel('Inland Cross-Shore Distance (Meters)', fontsize=10)
plt.grid(True, linestyle='--', alpha=0.5)

# Adicionar anotação técnica no gráfico para gestores do conselho regional
text_box = f"Flooding level: {total_flood_level:.2f}m\nTotal Area at Risk {flooded_area_pct:.1f}%"
plt.text(50, 900, text_box, fontsize=10, fontweight='bold', bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.5'))

# Salvar gráfico para integração no portfólio GitHub
plt.savefig('whangarei_coastal_flooding_map.png', dpi=150, bbox_inches='tight')
print("Success: 'whangarei_coastal_flooding_map.png' was generated successfully in your folder!")
