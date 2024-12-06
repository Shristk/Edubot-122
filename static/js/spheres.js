import Spheres2Background from 'https://cdn.jsdelivr.net/npm/threejs-components@0.0.8/build/backgrounds/spheres2.cdn.min.js';

const bg = Spheres2Background(document.getElementById('webgl-canvas'), {
    count: 200,
    colors: [0xff0000, 0x0, 0xffffff],
    minSize: 0.5,
    maxSize: 1
});

document.body.addEventListener('click', (ev) => {
    if (ev.target.id !== 'send-btn') bg.togglePause();
});
