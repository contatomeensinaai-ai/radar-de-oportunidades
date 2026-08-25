import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const pluginRoot = path.join(root, "plugins/radar-de-oportunidades");

function read(relativePath) {
  const fullPath = path.join(pluginRoot, relativePath);
  assert.ok(fs.existsSync(fullPath), `Arquivo ausente: ${relativePath}`);
  return fs.readFileSync(fullPath, "utf8");
}

const manifest = JSON.parse(read(".codex-plugin/plugin.json"));
assert.equal(manifest.name, "radar-de-oportunidades");
assert.equal(manifest.interface.displayName, "Radar de Oportunidades com IA");
assert.equal(manifest.interface.composerIcon, "./assets/icon.png");
assert.equal(manifest.interface.logo, "./assets/logo.png");

const skill = read("skills/rastrear-oportunidades/SKILL.md");
for (const phrase of [
  "Modo VIP",
  "Dossiê de Mercado",
  "dados comerciais públicos",
  "não envie mensagens",
  "LEADS-QUALIFICADOS.csv",
  "RADAR-DE-OPORTUNIDADES.md",
  "Browser Harness",
  "evidência",
]) {
  assert.ok(skill.toLowerCase().includes(phrase.toLowerCase()), `Contrato ausente na skill: ${phrase}`);
}

for (const file of [
  "skills/rastrear-oportunidades/references/criterios-de-qualificacao.md",
  "skills/rastrear-oportunidades/references/navegacao-segura.md",
  "skills/rastrear-oportunidades/templates/RADAR-DE-OPORTUNIDADES.md",
  "skills/rastrear-oportunidades/templates/LEADS-QUALIFICADOS.csv",
  "scripts/validate_radar_csv.py",
  "assets/icon.png",
  "assets/logo.png",
]) {
  assert.ok(fs.existsSync(path.join(pluginRoot, file)), `Arquivo ausente: ${file}`);
}

const marketplace = JSON.parse(fs.readFileSync(path.join(root, ".agents/plugins/marketplace.json"), "utf8"));
assert.ok(marketplace.plugins.some((plugin) => plugin.name === "radar-de-oportunidades"));

console.log("Radar de Oportunidades validado estruturalmente.");
