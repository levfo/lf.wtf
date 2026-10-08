// owner: render-world
// Section 9.2: ground picking. A ray is cast against y = 0, then refined twice against the terrain height.
import * as THREE from 'three';

// ndcX and ndcY are normalised device coordinates (-1..1). heightAt(tileX, tileY) gives the terrain height of a tile.
// Returns the tile under the ray (floor of the hit), or null when the ray does not reach the ground.
export function pickGround(threeCamera, ndcX, ndcY, heightAt) {
  threeCamera.updateMatrixWorld();
  const origin = new THREE.Vector3().setFromMatrixPosition(threeCamera.matrixWorld);
  const far = new THREE.Vector3(ndcX, ndcY, 0.5).unproject(threeCamera);
  const dir = far.sub(origin).normalize();
  if (!(Math.abs(dir.y) > 1e-9)) return null;

  let t = -origin.y / dir.y;
  if (!(t > 0)) return null;
  const hit = new THREE.Vector3();
  hit.copy(origin).addScaledVector(dir, t);

  for (let pass = 0; pass < 2; pass++) {
    const h = heightAt(Math.floor(hit.x), Math.floor(hit.z));
    t = (h - origin.y) / dir.y;
    if (!(t > 0)) return null;
    hit.copy(origin).addScaledVector(dir, t);
  }

  return { x: Math.floor(hit.x), y: Math.floor(hit.z) };
}
