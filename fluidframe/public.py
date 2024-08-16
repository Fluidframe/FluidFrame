
class _assets:
    fluidframe_logo_webp: str = "assets/fluidframe-logo.webp"
    clipboard_svg: str = "assets/clipboard.svg"

class _scripts:
    dependency_manager_js: str = "scripts/dependency_manager.js"
    highlight_code_js: str = "scripts/highlight_code.js"
    hot_reload_js: str = "scripts/hot_reload.js"
    tooltip_js: str = "scripts/tooltip.js"
    copy_code_js: str = "scripts/copy_code.js"

    class _scripts_prismjs:
        vendors_bundle_js: str = "scripts/prismjs/vendors.bundle.js"
        okaidia: str = "scripts/prismjs/okaidia/python_bundle.js"
    prismjs = _scripts_prismjs()


class Bundle:
    assets=_assets()
    scripts=_scripts()


js_bundle = Bundle()