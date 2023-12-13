import numpy as np
import matplotlib.pyplot as plt

# Defina a função do paraboloide
def func(x, y):
    return x**2 - y**4



n_para_curvas = 100

z_plot = 1

curvas_de_nivel = []
curvas_de_nivel_pre = []

if n_para_curvas == 1:
    curvas_de_nivel.append(z_plot)
    
else:
    if n_para_curvas//2 != n_para_curvas/2:
        curvas_de_nivel_pre.append(z_plot)
    
    for i in range(n_para_curvas//2+1):
        curvas_de_nivel_pre.append(z_plot-i)
        
    for i in range(n_para_curvas//2+1):
        curvas_de_nivel_pre.append(z_plot+i)
        
    curvas_de_nivel_pre.sort()
    
    for item in curvas_de_nivel_pre:
        if item not in curvas_de_nivel:
            curvas_de_nivel.append(item)
    
    curvas_de_nivel.sort()

print (curvas_de_nivel)



# Crie pontos de dados
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = func(x, y)

# Plotagem da superfície 3D
fig = plt.figure(figsize=(12, 5))

# Subtrama da superfície 3D
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x, y, z, cmap='viridis')
ax1.set_title('Paraboloide 3D')

# Subtrama da curva de nível
ax2 = fig.add_subplot(122)
contour_plot = ax2.contour(x, y, z, levels=curvas_de_nivel, colors='r')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')

if n_para_curvas == 1:
    ax2.set_title('Curva de Nível para z = {}'.format(z_plot))
else:
    ax2.set_title('Curvas de Nível em torno de z = {}'.format(z_plot))
    

# Adicione uma legenda para a curva de nível
ax2.clabel(contour_plot, inline=True, fontsize=8, colors='r')

# Exiba os gráficos
plt.tight_layout()
plt.show()
