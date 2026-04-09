PROJECT NAME: 3D Car Viewing Website

FILE TREE:
.
|-- index.html
|-- TECHNICAL_SPEC.md

TECH STACK:
- HTML5
- JavaScript (ES6+)
- Three.js r163 (for 3D rendering)
- Three.js GLTFLoader r163 (for loading 3D models)
- Three.js OrbitControls r163 (for drag-to-rotate interaction)

API ENDPOINT SIGNATURES:
N/A (Single HTML file, client-side JavaScript only)

DEPENDENCY LIST:
External CDN links to be included in index.html:
- Three.js: https://unpkg.com/three@0.163.0/build/three.min.js
- GLTFLoader: https://unpkg.com/three@0.163.0/examples/jsm/loaders/GLTFLoader.js
- OrbitControls: https://unpkg.com/three@0.163.0/examples/jsm/controls/OrbitControls.js

FEATURES:
1.  **3D Car Model Display**: Load and render a 3D car model (GLTF format).
2.  **Rotating View**: The car model will continuously rotate.
3.  **Drag-to-Rotate Interaction**: Users can drag the mouse to manually rotate the view of the car.
4.  **Star Background**: A starry background will be rendered behind the car.
5.  **Responsive Design**: The 3D scene will adapt to the browser window size.
