
class _assets:
    fluidframe_logo_webp: str = "assets/fluidframe-logo.webp"
    clipboard_svg: str = "assets/clipboard.svg"

class _scripts:
    fluidframe_bundle_js: str = "scripts/fluidframe.bundle.js"
    highlight_code_js: str = "scripts/highlight_code.js"
    hot_reload_js: str = "scripts/hot_reload.js"
    htmx_bundle_js: str = "scripts/htmx.bundle.js"
    tooltip_js: str = "scripts/tooltip.js"
    copy_code_js: str = "scripts/copy_code.js"

    class _scripts_prismjs:
        prism_php_bundle_js: str = "scripts/prismjs/prism-php.bundle.js"
        prism_typescript_bundle_js: str = "scripts/prismjs/prism-typescript.bundle.js"
        prism_markdown_bundle_js: str = "scripts/prismjs/prism-markdown.bundle.js"
        prism_scala_bundle_js: str = "scripts/prismjs/prism-scala.bundle.js"
        prism_json_bundle_js: str = "scripts/prismjs/prism-json.bundle.js"
        prism_kotlin_bundle_js: str = "scripts/prismjs/prism-kotlin.bundle.js"
        prism_javascript_bundle_js: str = "scripts/prismjs/prism-javascript.bundle.js"
        prism_haskell_bundle_js: str = "scripts/prismjs/prism-haskell.bundle.js"
        prism_sql_bundle_js: str = "scripts/prismjs/prism-sql.bundle.js"
        prism_bash_bundle_js: str = "scripts/prismjs/prism-bash.bundle.js"
        prism_dart_bundle_js: str = "scripts/prismjs/prism-dart.bundle.js"
        prism_lua_bundle_js: str = "scripts/prismjs/prism-lua.bundle.js"
        prism_python_bundle_js: str = "scripts/prismjs/prism-python.bundle.js"
        prism_objectivec_bundle_js: str = "scripts/prismjs/prism-objectivec.bundle.js"
        prism_less_bundle_js: str = "scripts/prismjs/prism-less.bundle.js"
        prism_markup_bundle_js: str = "scripts/prismjs/prism-markup.bundle.js"
        prism_rust_bundle_js: str = "scripts/prismjs/prism-rust.bundle.js"
        prism_csharp_bundle_js: str = "scripts/prismjs/prism-csharp.bundle.js"
        prism_r_bundle_js: str = "scripts/prismjs/prism-r.bundle.js"
        prism_perl_bundle_js: str = "scripts/prismjs/prism-perl.bundle.js"
        prism_java_bundle_js: str = "scripts/prismjs/prism-java.bundle.js"
        prism_go_bundle_js: str = "scripts/prismjs/prism-go.bundle.js"
        prism_cpp_bundle_js: str = "scripts/prismjs/prism-cpp.bundle.js"
        prism_css_bundle_js: str = "scripts/prismjs/prism-css.bundle.js"
        prism_yaml_bundle_js: str = "scripts/prismjs/prism-yaml.bundle.js"
        prism_ruby_bundle_js: str = "scripts/prismjs/prism-ruby.bundle.js"
        prism_xml_bundle_js: str = "scripts/prismjs/prism-xml.bundle.js"
        prism_zig_bundle_js: str = "scripts/prismjs/prism-zig.bundle.js"
        prism_sass_bundle_js: str = "scripts/prismjs/prism-sass.bundle.js"
        prism_swift_bundle_js: str = "scripts/prismjs/prism-swift.bundle.js"
    prismjs = _scripts_prismjs()

    class _scripts_fluidframe:
        dependency_manager_js: str = "scripts/fluidframe/dependency_manager.js"
        state_manager_js: str = "scripts/fluidframe/state_manager.js"
    fluidframe = _scripts_fluidframe()


class Bundle:
    assets=_assets()
    scripts=_scripts()


js_bundle = Bundle()