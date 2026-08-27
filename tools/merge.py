"""Fold the per-page translation modules into content/*.json, and say what is still missing."""
import importlib.util, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCALES = ["de", "es", "es-MX", "fr", "it", "ja", "ko", "nl", "pt-BR", "zh-Hans"]


def load(name):
    path = ROOT / "tools" / "lang" / f"{name}.py"
    if not path.exists():
        return {}, set()
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, "T", {}), set(getattr(mod, "KEEP", ()))


def main():
    total_missing = 0
    for f in sorted((ROOT / "content").glob("*.json")):
        data = json.loads(f.read_text())
        T, KEEP = load(f.stem)
        missing = []
        for en, entry in data.items():
            if en in KEEP:                       # brand names, handles, prices: same everywhere
                for loc in LOCALES:
                    entry[loc] = en
            elif en in T:
                values = T[en]
                assert len(values) == len(LOCALES), f"{f.stem}: {en[:40]!r} has {len(values)}"
                for loc, value in zip(LOCALES, values):
                    entry[loc] = value
            else:
                missing.append(en)
        f.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        total_missing += len(missing)
        state = "complete" if not missing else f"{len(missing)} missing"
        print(f"{f.stem:16} {len(data):3} segments  {state}")
        for m in missing[:4]:
            print(f"                   ... {m[:88]!r}")
    print(f"\n{total_missing} segments still untranslated")
    return 1 if total_missing else 0


if __name__ == "__main__":
    sys.exit(main())
