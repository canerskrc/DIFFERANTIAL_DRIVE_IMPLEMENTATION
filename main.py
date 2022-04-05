import numpy as np
def diffdrive(x, y, theta, v_l, v_r, t, l):

      # düz yol
      if (v_l == v_r):
            theta_n = theta
            x_n = x + v_l * t * np.cos(theta)
            y_n = y + v_l * t * np.sin(theta)
# dairesel hareket
      else:

# yarıçap hesabı
            R = l/2.0 * ((v_l + v_r) / (v_r - v_l))
# eğrilik merkezinin hesabı
            ICC_x = x - R * np.sin(theta)
            ICC_y = y + R * np.cos(theta)
# açısal hızın hesabı
            omega = (v_r - v_l) / l
# açı değişim hesabı
            dtheta = omega * t
# diferansiyel sürüş için kinematik
            x_n = np.cos(dtheta)*(x-ICC_x) - np.sin(dtheta)*(y-ICC_y) + ICC_x
            y_n = np.sin(dtheta)*(x-ICC_x) + np.cos(dtheta)*(y-ICC_y) + ICC_y
            theta_n = theta + dtheta
      return x_n, y_n, theta_n

import matplotlib.pyplot as plt
#from diffdrive import diffdrive
plt.gca().set_aspect("equal")
#tekerlekler ile robot konumu arasındaki mesafeyi ayarlama
l = 0.5
x, y, theta = 1.5, 2.0, (np.pi)/2.0
# başlangıç pozisyonunun plot yapılması
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print ("başlangıç pozisyonu: x: %f, y: %f, theta: %f" % (x, y, theta))
# ilk hareket
v_l = 0.3
v_r = 0.3
t = 3
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print ("ilk hareketten sonra: x: %f, y: %f, theta: %f" % (x, y, theta))
# ikinci hareket
v_l = 0.1
v_r = -0.1
t = 1
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print ("2. hareketten sonra: x: %f, y: %f, theta: %f" % (x, y, theta))
# üçüncü hareket
v_l = 0.2
v_r = 0.0
t = 2
x, y, theta = diffdrive(x, y, theta, v_l, v_r, t, l)
plt.quiver(x, y, np.cos(theta), np.sin(theta))
print ("3.hareketten sonra: x: %f, y: %f, theta: %f" % (x, y, theta))
plt.xlim([0.5, 2.5])
plt.ylim([1.5, 3.5])
plt.savefig("sheet3.png")
plt.show()
