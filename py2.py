import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from sklearn.decomposition import PCA


image_raw = imread("tiger.jpg")
print(image_raw.shape)

image_sum = image_raw.sum(axis=2)
print(image_sum.shape)

image_bw = image_sum/image_sum.max()
print(image_bw.max())

plt.imshow(image_bw, cmap='gray')
plt.show()

print(image_bw.shape)
print(image_bw.max())

pca = PCA(n_components=400)
pca.fit_transform(image_bw)

explained_variance = pca.explained_variance_ratio_
components = np.arange(len(explained_variance))
percent = np.array(explained_variance) * 100

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)
ax.set_title('Variance за числом компонентв')
ax.set_ylabel('% variance')
ax.set_xlabel('Кількість PCA компонентів')
ax.plot(components, np.cumsum(percent))

perf_component_count = 0


for variance in np.cumsum(percent):
    perf_component_count += 1
    if variance >= 95:
        plt.axvline(x=perf_component_count, color='black', linestyle=":")
        break
plt.axhline(y=95, color='r', linestyle=':')
plt.show()

pca_ideal = PCA(n_components=perf_component_count)
compressed = pca_ideal.fit_transform(image_bw)
decompressed = pca_ideal.inverse_transform(compressed)




fig, axes = plt.subplots(1, 2, figsize=(10, 5))
axes[0].imshow(image_bw)
axes[0].set_title("Початкове")
axes[1].imshow(decompressed)
axes[1].set_title(f"Компоненти: {perf_component_count}")
plt.show()

fig2, axes2 = plt.subplots(2, 3, figsize=(12, 8))

#
pca5 = PCA(n_components=5)
compressed = pca5.fit_transform(image_bw)
decompressed = pca5.inverse_transform(compressed)
axes2[0, 0].imshow(decompressed)
axes2[0, 0].set_title("5 компонентів")

pca10 = PCA(n_components=10)
compressed = pca10.fit_transform(image_bw)
decompressed = pca10.inverse_transform(compressed)
axes2[0, 1].imshow(decompressed)
axes2[0, 1].set_title("15 компонентів")

pca30 = PCA(n_components=30)
compressed = pca30.fit_transform(image_bw)
decompressed = pca30.inverse_transform(compressed)
axes2[0, 2].imshow(decompressed)
axes2[0, 2].set_title("30 компонентів")

pca50 = PCA(n_components=50)
compressed = pca50.fit_transform(image_bw)
decompressed = pca50.inverse_transform(compressed)
axes2[1, 0].imshow(decompressed)
axes2[1, 0].set_title("50 компонентів")

pca70 = PCA(n_components=70)
compressed = pca70.fit_transform(image_bw)
decompressed = pca70.inverse_transform(compressed)
axes2[1, 1].imshow(decompressed)
axes2[1, 1].set_title("70 компонентів")

pca100 = PCA(n_components=100)
compressed = pca100.fit_transform(image_bw)
decompressed = pca100.inverse_transform(compressed)
axes2[1, 2].imshow(decompressed)
axes2[1, 2].set_title("100 компонентів")

plt.show()