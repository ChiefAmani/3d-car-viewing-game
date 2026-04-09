# TECHNICAL_SPEC.md

## Project Name
3D Car Viewer

## File Tree
.
|-- index.html
|-- TECHNICAL_SPEC.md

## Tech Stack
*   HTML5
*   JavaScript
*   Three.js (r128 via CDN)
*   GLTFLoader (Three.js example, r128 via CDN)
*   OrbitControls (Three.js example, r128 via CDN)

## API Endpoint Signatures
N/A (This project is a single HTML file with client-side rendering and no backend API interactions.)

## Dependency List
*   Three.js: https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js
*   GLTFLoader: https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/examples/js/loaders/GLTFLoader.min.js
*   OrbitControls: https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/examples/js/controls/OrbitControls.min.js

## Implementation Details

### 1. HTML Structure (index.html)
The `index.html` file will contain a basic HTML5 structure with a `<canvas>` element for Three.js rendering. All JavaScript code will be embedded directly within a `<script>` tag in the `<body>` or linked as an external script.

### 2. Three.js Scene Setup
*   **Scene:** A `THREE.Scene` will be initialized.
*   **Camera:** A `THREE.PerspectiveCamera` will be used, positioned to view the car model.
*   **Renderer:** A `THREE.WebGLRenderer` will be created and attached to the HTML canvas.
*   **Lighting:** Basic ambient and directional lighting will be added to illuminate the 3D model.

### 3. 3D Model Loading (Car)
*   The `GLTFLoader` will be used to load a 3D car model in GLTF format.
*   The loaded model will be added to the Three.js scene.
*   A placeholder car model will be assumed for initial development.

### 4. Drag-to-Rotate Functionality
*   `THREE.OrbitControls` will be instantiated, linking the camera and the renderer's DOM element.
*   This will enable intuitive drag-to-rotate, zoom, and pan interactions with the scene, centered around the car model.

### 5. Starfield Background
*   A starfield will be created using `THREE.Points`.
*   A `THREE.BufferGeometry` will be populated with a large number of random 3D coordinates to represent stars.
*   A `THREE.PointsMaterial` with a small point size and white color will be applied to render these points as stars.
*   The starfield will be added to the scene.

### 6. Animation Loop
*   An animation loop using `requestAnimationFrame` will continuously render the scene.
*   Inside the loop, `OrbitControls.update()` will be called to handle camera movement, and the renderer will render the scene.
*   The car model will have a subtle continuous rotation animation.
