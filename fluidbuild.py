
class _node_modules:
    micromatch: str = "node_modules/micromatch/index.js"

    class _node_modules_supports_preserve_symlinks_flag:
        index_js: str = "node_modules/supports-preserve-symlinks-flag/index.js"
        browser_js: str = "node_modules/supports-preserve-symlinks-flag/browser.js"
        test: str = "node_modules/supports-preserve-symlinks-flag/test/index.js"
    supports_preserve_symlinks_flag = _node_modules_supports_preserve_symlinks_flag()

    class _node_modules_nth_check:

        class _node_modules_nth_check_lib:
            parse_js: str = "node_modules/nth-check/lib/parse.js"
            index_js: str = "node_modules/nth-check/lib/index.js"
            compile_js: str = "node_modules/nth-check/lib/compile.js"

            class _node_modules_nth_check_lib_esm:
                parse_js: str = "node_modules/nth-check/lib/esm/parse.js"
                index_js: str = "node_modules/nth-check/lib/esm/index.js"
                compile_js: str = "node_modules/nth-check/lib/esm/compile.js"
            esm = _node_modules_nth_check_lib_esm()
        lib = _node_modules_nth_check_lib()
    nth_check = _node_modules_nth_check()
    p_timeout: str = "node_modules/p-timeout/index.js"

    class _node_modules_chalk:

        class _node_modules_chalk_source:
            templates_js: str = "node_modules/chalk/source/templates.js"
            index_js: str = "node_modules/chalk/source/index.js"
            util_js: str = "node_modules/chalk/source/util.js"
        source = _node_modules_chalk_source()
    chalk = _node_modules_chalk()
    normalize_path: str = "node_modules/normalize-path/index.js"
    arg: str = "node_modules/arg/index.js"

    class _node_modules_css_what:

        class _node_modules_css_what_lib:

            class _node_modules_css_what_lib_commonjs:
                parse_js: str = "node_modules/css-what/lib/commonjs/parse.js"
                index_js: str = "node_modules/css-what/lib/commonjs/index.js"
                stringify_js: str = "node_modules/css-what/lib/commonjs/stringify.js"
                types_js: str = "node_modules/css-what/lib/commonjs/types.js"
            commonjs = _node_modules_css_what_lib_commonjs()

            class _node_modules_css_what_lib_es:
                parse_js: str = "node_modules/css-what/lib/es/parse.js"
                index_js: str = "node_modules/css-what/lib/es/index.js"
                stringify_js: str = "node_modules/css-what/lib/es/stringify.js"
                types_js: str = "node_modules/css-what/lib/es/types.js"
            es = _node_modules_css_what_lib_es()
        lib = _node_modules_css_what_lib()
    css_what = _node_modules_css_what()
    ansi_styles: str = "node_modules/ansi-styles/index.js"
    is_fullwidth_code_point: str = "node_modules/is-fullwidth-code-point/index.js"

    class _node_modules_postcss_value_parser:

        class _node_modules_postcss_value_parser_lib:
            parse_js: str = "node_modules/postcss-value-parser/lib/parse.js"
            walk_js: str = "node_modules/postcss-value-parser/lib/walk.js"
            unit_js: str = "node_modules/postcss-value-parser/lib/unit.js"
            index_js: str = "node_modules/postcss-value-parser/lib/index.js"
            stringify_js: str = "node_modules/postcss-value-parser/lib/stringify.js"
        lib = _node_modules_postcss_value_parser_lib()
    postcss_value_parser = _node_modules_postcss_value_parser()
    path_parse: str = "node_modules/path-parse/index.js"

    class _node_modules_camelcase_css:
        index_es5_js: str = "node_modules/camelcase-css/index-es5.js"
        index_js: str = "node_modules/camelcase-css/index.js"
    camelcase_css = _node_modules_camelcase_css()

    class _node_modules_alloc:
        quick_lru: str = "node_modules/@alloc/quick-lru/index.js"
    alloc = _node_modules_alloc()

    class _node_modules_minipass:

        class _node_modules_minipass_dist:
            esm: str = "node_modules/minipass/dist/esm/index.js"
            commonjs: str = "node_modules/minipass/dist/commonjs/index.js"
        dist = _node_modules_minipass_dist()
    minipass = _node_modules_minipass()

    class _node_modules_nanoid:
        nanoid_js: str = "node_modules/nanoid/nanoid.js"
        index_browser_js: str = "node_modules/nanoid/index.browser.js"
        index_js: str = "node_modules/nanoid/index.js"
        url_alphabet: str = "node_modules/nanoid/url-alphabet/index.js"
        non_secure: str = "node_modules/nanoid/non-secure/index.js"

        class _node_modules_nanoid_v_async:
            index_browser_js: str = "node_modules/nanoid/async/index.browser.js"
            index_js: str = "node_modules/nanoid/async/index.js"
            index_native_js: str = "node_modules/nanoid/async/index.native.js"
        v_async = _node_modules_nanoid_v_async()
    nanoid = _node_modules_nanoid()

    class _node_modules_source_map_js:
        source_map_js: str = "node_modules/source-map-js/source-map.js"

        class _node_modules_source_map_js_lib:
            source_map_generator_js: str = "node_modules/source-map-js/lib/source-map-generator.js"
            quick_sort_js: str = "node_modules/source-map-js/lib/quick-sort.js"
            mapping_list_js: str = "node_modules/source-map-js/lib/mapping-list.js"
            source_node_js: str = "node_modules/source-map-js/lib/source-node.js"
            util_js: str = "node_modules/source-map-js/lib/util.js"
            base64_js: str = "node_modules/source-map-js/lib/base64.js"
            binary_search_js: str = "node_modules/source-map-js/lib/binary-search.js"
            source_map_consumer_js: str = "node_modules/source-map-js/lib/source-map-consumer.js"
            array_set_js: str = "node_modules/source-map-js/lib/array-set.js"
            base64_vlq_js: str = "node_modules/source-map-js/lib/base64-vlq.js"
        lib = _node_modules_source_map_js_lib()
    source_map_js = _node_modules_source_map_js()

    class _node_modules_postcss_minify_params:
        src: str = "node_modules/postcss-minify-params/src/index.js"
    postcss_minify_params = _node_modules_postcss_minify_params()

    class _node_modules_which:
        which_js: str = "node_modules/which/which.js"
    which = _node_modules_which()

    class _node_modules_update_browserslist_db:
        utils_js: str = "node_modules/update-browserslist-db/utils.js"
        cli_js: str = "node_modules/update-browserslist-db/cli.js"
        check_npm_version_js: str = "node_modules/update-browserslist-db/check-npm-version.js"
        index_js: str = "node_modules/update-browserslist-db/index.js"
    update_browserslist_db = _node_modules_update_browserslist_db()

    class _node_modules_function_bind:
        implementation_js: str = "node_modules/function-bind/implementation.js"
        index_js: str = "node_modules/function-bind/index.js"
        test: str = "node_modules/function-bind/test/index.js"
    function_bind = _node_modules_function_bind()

    class _node_modules_string_width_cjs:
        index_js: str = "node_modules/string-width-cjs/index.js"

        class _node_modules_string_width_cjs_node_modules:
            strip_ansi: str = "node_modules/string-width-cjs/node_modules/strip-ansi/index.js"
            ansi_regex: str = "node_modules/string-width-cjs/node_modules/ansi-regex/index.js"

            class _node_modules_string_width_cjs_node_modules_emoji_regex:
                text_js: str = "node_modules/string-width-cjs/node_modules/emoji-regex/text.js"
                index_js: str = "node_modules/string-width-cjs/node_modules/emoji-regex/index.js"

                class _node_modules_string_width_cjs_node_modules_emoji_regex_es2015:
                    text_js: str = "node_modules/string-width-cjs/node_modules/emoji-regex/es2015/text.js"
                    index_js: str = "node_modules/string-width-cjs/node_modules/emoji-regex/es2015/index.js"
                es2015 = _node_modules_string_width_cjs_node_modules_emoji_regex_es2015()
            emoji_regex = _node_modules_string_width_cjs_node_modules_emoji_regex()
        node_modules = _node_modules_string_width_cjs_node_modules()
    string_width_cjs = _node_modules_string_width_cjs()

    class _node_modules_postcss_selector_parser:

        class _node_modules_postcss_selector_parser_dist:
            sortAscending_js: str = "node_modules/postcss-selector-parser/dist/sortAscending.js"
            parser_js: str = "node_modules/postcss-selector-parser/dist/parser.js"
            index_js: str = "node_modules/postcss-selector-parser/dist/index.js"
            tokenize_js: str = "node_modules/postcss-selector-parser/dist/tokenize.js"
            tokenTypes_js: str = "node_modules/postcss-selector-parser/dist/tokenTypes.js"
            processor_js: str = "node_modules/postcss-selector-parser/dist/processor.js"

            class _node_modules_postcss_selector_parser_dist_util:
                unesc_js: str = "node_modules/postcss-selector-parser/dist/util/unesc.js"
                index_js: str = "node_modules/postcss-selector-parser/dist/util/index.js"
                stripComments_js: str = "node_modules/postcss-selector-parser/dist/util/stripComments.js"
                getProp_js: str = "node_modules/postcss-selector-parser/dist/util/getProp.js"
                ensureObject_js: str = "node_modules/postcss-selector-parser/dist/util/ensureObject.js"
            util = _node_modules_postcss_selector_parser_dist_util()

            class _node_modules_postcss_selector_parser_dist_selectors:
                comment_js: str = "node_modules/postcss-selector-parser/dist/selectors/comment.js"
                pseudo_js: str = "node_modules/postcss-selector-parser/dist/selectors/pseudo.js"
                combinator_js: str = "node_modules/postcss-selector-parser/dist/selectors/combinator.js"
                string_js: str = "node_modules/postcss-selector-parser/dist/selectors/string.js"
                attribute_js: str = "node_modules/postcss-selector-parser/dist/selectors/attribute.js"
                className_js: str = "node_modules/postcss-selector-parser/dist/selectors/className.js"
                nesting_js: str = "node_modules/postcss-selector-parser/dist/selectors/nesting.js"
                namespace_js: str = "node_modules/postcss-selector-parser/dist/selectors/namespace.js"
                guards_js: str = "node_modules/postcss-selector-parser/dist/selectors/guards.js"
                index_js: str = "node_modules/postcss-selector-parser/dist/selectors/index.js"
                node_js: str = "node_modules/postcss-selector-parser/dist/selectors/node.js"
                root_js: str = "node_modules/postcss-selector-parser/dist/selectors/root.js"
                universal_js: str = "node_modules/postcss-selector-parser/dist/selectors/universal.js"
                container_js: str = "node_modules/postcss-selector-parser/dist/selectors/container.js"
                tag_js: str = "node_modules/postcss-selector-parser/dist/selectors/tag.js"
                selector_js: str = "node_modules/postcss-selector-parser/dist/selectors/selector.js"
                constructors_js: str = "node_modules/postcss-selector-parser/dist/selectors/constructors.js"
                types_js: str = "node_modules/postcss-selector-parser/dist/selectors/types.js"
                id_js: str = "node_modules/postcss-selector-parser/dist/selectors/id.js"
            selectors = _node_modules_postcss_selector_parser_dist_selectors()
        dist = _node_modules_postcss_selector_parser_dist()
    postcss_selector_parser = _node_modules_postcss_selector_parser()
    promise_series: str = "node_modules/promise.series/index.js"

    class _node_modules_caniuse_api:

        class _node_modules_caniuse_api_dist:
            utils_js: str = "node_modules/caniuse-api/dist/utils.js"
            index_js: str = "node_modules/caniuse-api/dist/index.js"
        dist = _node_modules_caniuse_api_dist()
    caniuse_api = _node_modules_caniuse_api()

    class _node_modules_postcss_normalize_repeat_style:

        class _node_modules_postcss_normalize_repeat_style_src:
            index_js: str = "node_modules/postcss-normalize-repeat-style/src/index.js"
            lib: str = "node_modules/postcss-normalize-repeat-style/src/lib/map.js"
        src = _node_modules_postcss_normalize_repeat_style_src()
    postcss_normalize_repeat_style = _node_modules_postcss_normalize_repeat_style()

    class _node_modules_fastq:
        example_js: str = "node_modules/fastq/example.js"
        bench_js: str = "node_modules/fastq/bench.js"
        queue_js: str = "node_modules/fastq/queue.js"

        class _node_modules_fastq_test:
            test_js: str = "node_modules/fastq/test/test.js"
            promise_js: str = "node_modules/fastq/test/promise.js"
        test = _node_modules_fastq_test()
    fastq = _node_modules_fastq()

    class _node_modules_string_hash:
        test_js: str = "node_modules/string-hash/test.js"
        index_js: str = "node_modules/string-hash/index.js"
    string_hash = _node_modules_string_hash()
    concat_with_sourcemaps: str = "node_modules/concat-with-sourcemaps/index.js"
    is_binary_path: str = "node_modules/is-binary-path/index.js"
    is_module: str = "node_modules/is-module/index.js"

    class _node_modules_loader_utils:

        class _node_modules_loader_utils_lib:
            urlToRequest_js: str = "node_modules/loader-utils/lib/urlToRequest.js"
            interpolateName_js: str = "node_modules/loader-utils/lib/interpolateName.js"
            index_js: str = "node_modules/loader-utils/lib/index.js"
            getHashDigest_js: str = "node_modules/loader-utils/lib/getHashDigest.js"
            isUrlRequest_js: str = "node_modules/loader-utils/lib/isUrlRequest.js"

            class _node_modules_loader_utils_lib_hash:
                BulkUpdateDecorator_js: str = "node_modules/loader-utils/lib/hash/BulkUpdateDecorator.js"
                md4_js: str = "node_modules/loader-utils/lib/hash/md4.js"
                BatchedHash_js: str = "node_modules/loader-utils/lib/hash/BatchedHash.js"
                xxhash64_js: str = "node_modules/loader-utils/lib/hash/xxhash64.js"
                wasm_hash_js: str = "node_modules/loader-utils/lib/hash/wasm-hash.js"
            hash = _node_modules_loader_utils_lib_hash()
        lib = _node_modules_loader_utils_lib()
    loader_utils = _node_modules_loader_utils()
    glob_parent: str = "node_modules/glob-parent/index.js"
    serialize_javascript: str = "node_modules/serialize-javascript/index.js"

    class _node_modules_postcss_merge_longhand:

        class _node_modules_postcss_merge_longhand_src:
            index_js: str = "node_modules/postcss-merge-longhand/src/index.js"

            class _node_modules_postcss_merge_longhand_src_lib:
                getValue_js: str = "node_modules/postcss-merge-longhand/src/lib/getValue.js"
                getLastNode_js: str = "node_modules/postcss-merge-longhand/src/lib/getLastNode.js"
                canMerge_js: str = "node_modules/postcss-merge-longhand/src/lib/canMerge.js"
                getDecls_js: str = "node_modules/postcss-merge-longhand/src/lib/getDecls.js"
                hasAllProps_js: str = "node_modules/postcss-merge-longhand/src/lib/hasAllProps.js"
                getRules_js: str = "node_modules/postcss-merge-longhand/src/lib/getRules.js"
                colornames_js: str = "node_modules/postcss-merge-longhand/src/lib/colornames.js"
                minifyWsc_js: str = "node_modules/postcss-merge-longhand/src/lib/minifyWsc.js"
                parseTrbl_js: str = "node_modules/postcss-merge-longhand/src/lib/parseTrbl.js"
                mergeValues_js: str = "node_modules/postcss-merge-longhand/src/lib/mergeValues.js"
                isCustomProp_js: str = "node_modules/postcss-merge-longhand/src/lib/isCustomProp.js"
                canExplode_js: str = "node_modules/postcss-merge-longhand/src/lib/canExplode.js"
                parseWsc_js: str = "node_modules/postcss-merge-longhand/src/lib/parseWsc.js"
                validateWsc_js: str = "node_modules/postcss-merge-longhand/src/lib/validateWsc.js"
                mergeRules_js: str = "node_modules/postcss-merge-longhand/src/lib/mergeRules.js"
                trbl_js: str = "node_modules/postcss-merge-longhand/src/lib/trbl.js"
                minifyTrbl_js: str = "node_modules/postcss-merge-longhand/src/lib/minifyTrbl.js"
                insertCloned_js: str = "node_modules/postcss-merge-longhand/src/lib/insertCloned.js"

                class _node_modules_postcss_merge_longhand_src_lib_decl:
                    borders_js: str = "node_modules/postcss-merge-longhand/src/lib/decl/borders.js"
                    padding_js: str = "node_modules/postcss-merge-longhand/src/lib/decl/padding.js"
                    index_js: str = "node_modules/postcss-merge-longhand/src/lib/decl/index.js"
                    columns_js: str = "node_modules/postcss-merge-longhand/src/lib/decl/columns.js"
                    margin_js: str = "node_modules/postcss-merge-longhand/src/lib/decl/margin.js"
                    boxBase_js: str = "node_modules/postcss-merge-longhand/src/lib/decl/boxBase.js"
                decl = _node_modules_postcss_merge_longhand_src_lib_decl()
            lib = _node_modules_postcss_merge_longhand_src_lib()
        src = _node_modules_postcss_merge_longhand_src()
    postcss_merge_longhand = _node_modules_postcss_merge_longhand()

    class _node_modules_dlv:
        index_js: str = "node_modules/dlv/index.js"

        class _node_modules_dlv_dist:
            dlv_umd_js: str = "node_modules/dlv/dist/dlv.umd.js"
            dlv_es_js: str = "node_modules/dlv/dist/dlv.es.js"
            dlv_js: str = "node_modules/dlv/dist/dlv.js"
        dist = _node_modules_dlv_dist()
    dlv = _node_modules_dlv()

    class _node_modules_ts_interface_checker:

        class _node_modules_ts_interface_checker_dist:
            index_js: str = "node_modules/ts-interface-checker/dist/index.js"
            util_js: str = "node_modules/ts-interface-checker/dist/util.js"
            types_js: str = "node_modules/ts-interface-checker/dist/types.js"
        dist = _node_modules_ts_interface_checker_dist()
    ts_interface_checker = _node_modules_ts_interface_checker()

    class _node_modules_postcss_modules_local_by_default:
        src: str = "node_modules/postcss-modules-local-by-default/src/index.js"
    postcss_modules_local_by_default = _node_modules_postcss_modules_local_by_default()

    class _node_modules_postcss_reduce_initial:

        class _node_modules_postcss_reduce_initial_src:
            index_js: str = "node_modules/postcss-reduce-initial/src/index.js"
        src = _node_modules_postcss_reduce_initial_src()
    postcss_reduce_initial = _node_modules_postcss_reduce_initial()

    class _node_modules_resolve:
        async_js: str = "node_modules/resolve/async.js"
        index_js: str = "node_modules/resolve/index.js"
        sync_js: str = "node_modules/resolve/sync.js"

        class _node_modules_resolve_example:
            async_js: str = "node_modules/resolve/example/async.js"
            sync_js: str = "node_modules/resolve/example/sync.js"
        example = _node_modules_resolve_example()

        class _node_modules_resolve_test:
            faulty_basedir_js: str = "node_modules/resolve/test/faulty_basedir.js"
            node_modules_paths_js: str = "node_modules/resolve/test/node-modules-paths.js"
            symlinks_js: str = "node_modules/resolve/test/symlinks.js"
            node_path_js: str = "node_modules/resolve/test/node_path.js"
            subdirs_js: str = "node_modules/resolve/test/subdirs.js"
            module_dir_js: str = "node_modules/resolve/test/module_dir.js"
            precedence_js: str = "node_modules/resolve/test/precedence.js"
            filter_js: str = "node_modules/resolve/test/filter.js"
            shadowed_core_js: str = "node_modules/resolve/test/shadowed_core.js"
            pathfilter_js: str = "node_modules/resolve/test/pathfilter.js"
            mock_js: str = "node_modules/resolve/test/mock.js"
            mock_sync_js: str = "node_modules/resolve/test/mock_sync.js"
            core_js: str = "node_modules/resolve/test/core.js"
            nonstring_js: str = "node_modules/resolve/test/nonstring.js"
            resolver_sync_js: str = "node_modules/resolve/test/resolver_sync.js"
            home_paths_js: str = "node_modules/resolve/test/home_paths.js"
            dotdot_js: str = "node_modules/resolve/test/dotdot.js"
            filter_sync_js: str = "node_modules/resolve/test/filter_sync.js"
            home_paths_sync_js: str = "node_modules/resolve/test/home_paths_sync.js"
            resolver_js: str = "node_modules/resolve/test/resolver.js"

            class _node_modules_resolve_test_module_dir:

                class _node_modules_resolve_test_module_dir_xmodules:
                    aaa: str = "node_modules/resolve/test/module_dir/xmodules/aaa/index.js"
                xmodules = _node_modules_resolve_test_module_dir_xmodules()

                class _node_modules_resolve_test_module_dir_ymodules:
                    aaa: str = "node_modules/resolve/test/module_dir/ymodules/aaa/index.js"
                ymodules = _node_modules_resolve_test_module_dir_ymodules()

                class _node_modules_resolve_test_module_dir_zmodules:
                    bbb: str = "node_modules/resolve/test/module_dir/zmodules/bbb/main.js"
                zmodules = _node_modules_resolve_test_module_dir_zmodules()
            module_dir = _node_modules_resolve_test_module_dir()

            class _node_modules_resolve_test_precedence:
                aaa_js: str = "node_modules/resolve/test/precedence/aaa.js"
                bbb_js: str = "node_modules/resolve/test/precedence/bbb.js"

                class _node_modules_resolve_test_precedence_aaa:
                    index_js: str = "node_modules/resolve/test/precedence/aaa/index.js"
                    main_js: str = "node_modules/resolve/test/precedence/aaa/main.js"
                aaa = _node_modules_resolve_test_precedence_aaa()
                bbb: str = "node_modules/resolve/test/precedence/bbb/main.js"
            precedence = _node_modules_resolve_test_precedence()

            class _node_modules_resolve_test_dotdot:
                index_js: str = "node_modules/resolve/test/dotdot/index.js"
                abc: str = "node_modules/resolve/test/dotdot/abc/index.js"
            dotdot = _node_modules_resolve_test_dotdot()

            class _node_modules_resolve_test_resolver:
                mug_js: str = "node_modules/resolve/test/resolver/mug.js"
                foo_js: str = "node_modules/resolve/test/resolver/foo.js"
                false_main: str = "node_modules/resolve/test/resolver/false_main/index.js"
                incorrect_main: str = "node_modules/resolve/test/resolver/incorrect_main/index.js"

                class _node_modules_resolve_test_resolver_browser_field:
                    a_js: str = "node_modules/resolve/test/resolver/browser_field/a.js"
                    b_js: str = "node_modules/resolve/test/resolver/browser_field/b.js"
                browser_field = _node_modules_resolve_test_resolver_browser_field()

                class _node_modules_resolve_test_resolver_nested_symlinks:

                    class _node_modules_resolve_test_resolver_nested_symlinks_mylib:
                        async_js: str = "node_modules/resolve/test/resolver/nested_symlinks/mylib/async.js"
                        sync_js: str = "node_modules/resolve/test/resolver/nested_symlinks/mylib/sync.js"
                    mylib = _node_modules_resolve_test_resolver_nested_symlinks_mylib()
                nested_symlinks = _node_modules_resolve_test_resolver_nested_symlinks()
                without_basedir: str = "node_modules/resolve/test/resolver/without_basedir/main.js"

                class _node_modules_resolve_test_resolver_baz:
                    doom_js: str = "node_modules/resolve/test/resolver/baz/doom.js"
                    quux_js: str = "node_modules/resolve/test/resolver/baz/quux.js"
                baz = _node_modules_resolve_test_resolver_baz()

                class _node_modules_resolve_test_resolver_other_path:
                    root_js: str = "node_modules/resolve/test/resolver/other_path/root.js"
                    lib: str = "node_modules/resolve/test/resolver/other_path/lib/other-lib.js"
                other_path = _node_modules_resolve_test_resolver_other_path()

                class _node_modules_resolve_test_resolver_symlinked:
                    package: str = "node_modules/resolve/test/resolver/symlinked/package/bar.js"

                    class _node_modules_resolve_test_resolver_symlinked__:
                        node_modules: str = "node_modules/resolve/test/resolver/symlinked/_/node_modules/foo.js"
                    _ = _node_modules_resolve_test_resolver_symlinked__()
                symlinked = _node_modules_resolve_test_resolver_symlinked()
                dot_main: str = "node_modules/resolve/test/resolver/dot_main/index.js"
                dot_slash_main: str = "node_modules/resolve/test/resolver/dot_slash_main/index.js"

                class _node_modules_resolve_test_resolver_multirepo:

                    class _node_modules_resolve_test_resolver_multirepo_packages:
                        package_a: str = "node_modules/resolve/test/resolver/multirepo/packages/package-a/index.js"
                        package_b: str = "node_modules/resolve/test/resolver/multirepo/packages/package-b/index.js"
                    packages = _node_modules_resolve_test_resolver_multirepo_packages()
                multirepo = _node_modules_resolve_test_resolver_multirepo()

                class _node_modules_resolve_test_resolver_same_names:
                    foo_js: str = "node_modules/resolve/test/resolver/same_names/foo.js"
                    foo: str = "node_modules/resolve/test/resolver/same_names/foo/index.js"
                same_names = _node_modules_resolve_test_resolver_same_names()

                class _node_modules_resolve_test_resolver_quux:
                    foo: str = "node_modules/resolve/test/resolver/quux/foo/index.js"
                quux = _node_modules_resolve_test_resolver_quux()
            resolver = _node_modules_resolve_test_resolver()

            class _node_modules_resolve_test_pathfilter:
                deep_ref: str = "node_modules/resolve/test/pathfilter/deep_ref/main.js"
            pathfilter = _node_modules_resolve_test_pathfilter()

            class _node_modules_resolve_test_shadowed_core:

                class _node_modules_resolve_test_shadowed_core_node_modules:
                    util: str = "node_modules/resolve/test/shadowed_core/node_modules/util/index.js"
                node_modules = _node_modules_resolve_test_shadowed_core_node_modules()
            shadowed_core = _node_modules_resolve_test_shadowed_core()

            class _node_modules_resolve_test_node_path:

                class _node_modules_resolve_test_node_path_y:
                    ccc: str = "node_modules/resolve/test/node_path/y/ccc/index.js"
                    bbb: str = "node_modules/resolve/test/node_path/y/bbb/index.js"
                y = _node_modules_resolve_test_node_path_y()

                class _node_modules_resolve_test_node_path_x:
                    ccc: str = "node_modules/resolve/test/node_path/x/ccc/index.js"
                    aaa: str = "node_modules/resolve/test/node_path/x/aaa/index.js"
                x = _node_modules_resolve_test_node_path_x()
            node_path = _node_modules_resolve_test_node_path()
        test = _node_modules_resolve_test()

        class _node_modules_resolve_lib:
            async_js: str = "node_modules/resolve/lib/async.js"
            node_modules_paths_js: str = "node_modules/resolve/lib/node-modules-paths.js"
            normalize_options_js: str = "node_modules/resolve/lib/normalize-options.js"
            homedir_js: str = "node_modules/resolve/lib/homedir.js"
            is_core_js: str = "node_modules/resolve/lib/is-core.js"
            core_js: str = "node_modules/resolve/lib/core.js"
            caller_js: str = "node_modules/resolve/lib/caller.js"
            sync_js: str = "node_modules/resolve/lib/sync.js"
        lib = _node_modules_resolve_lib()
    resolve = _node_modules_resolve()

    class _node_modules_is_reference:

        class _node_modules_is_reference_dist:
            is_reference_es_js: str = "node_modules/is-reference/dist/is-reference.es.js"
            is_reference_js: str = "node_modules/is-reference/dist/is-reference.js"
        dist = _node_modules_is_reference_dist()
    is_reference = _node_modules_is_reference()

    class _node_modules_postcss_normalize_display_values:

        class _node_modules_postcss_normalize_display_values_src:
            index_js: str = "node_modules/postcss-normalize-display-values/src/index.js"
            lib: str = "node_modules/postcss-normalize-display-values/src/lib/map.js"
        src = _node_modules_postcss_normalize_display_values_src()
    postcss_normalize_display_values = _node_modules_postcss_normalize_display_values()

    class _node_modules_postcss_modules_values:
        src: str = "node_modules/postcss-modules-values/src/index.js"
    postcss_modules_values = _node_modules_postcss_modules_values()

    class _node_modules_domhandler:

        class _node_modules_domhandler_lib:
            index_js: str = "node_modules/domhandler/lib/index.js"
            node_js: str = "node_modules/domhandler/lib/node.js"
        lib = _node_modules_domhandler_lib()
    domhandler = _node_modules_domhandler()
    strip_ansi: str = "node_modules/strip-ansi/index.js"

    class _node_modules_deepmerge:
        index_js: str = "node_modules/deepmerge/index.js"
        rollup_config_js: str = "node_modules/deepmerge/rollup.config.js"

        class _node_modules_deepmerge_dist:
            cjs_js: str = "node_modules/deepmerge/dist/cjs.js"
            umd_js: str = "node_modules/deepmerge/dist/umd.js"
        dist = _node_modules_deepmerge_dist()
    deepmerge = _node_modules_deepmerge()
    is_extglob: str = "node_modules/is-extglob/index.js"
    lodash_memoize: str = "node_modules/lodash.memoize/index.js"

    class _node_modules_escalade:
        sync: str = "node_modules/escalade/sync/index.js"
        dist: str = "node_modules/escalade/dist/index.js"
    escalade = _node_modules_escalade()

    class _node_modules_postcss_merge_rules:

        class _node_modules_postcss_merge_rules_src:
            index_js: str = "node_modules/postcss-merge-rules/src/index.js"
            lib: str = "node_modules/postcss-merge-rules/src/lib/ensureCompatibility.js"
        src = _node_modules_postcss_merge_rules_src()
    postcss_merge_rules = _node_modules_postcss_merge_rules()

    class _node_modules_postcss_minify_font_values:

        class _node_modules_postcss_minify_font_values_src:
            index_js: str = "node_modules/postcss-minify-font-values/src/index.js"

            class _node_modules_postcss_minify_font_values_src_lib:
                minify_weight_js: str = "node_modules/postcss-minify-font-values/src/lib/minify-weight.js"
                minify_font_js: str = "node_modules/postcss-minify-font-values/src/lib/minify-font.js"
                minify_family_js: str = "node_modules/postcss-minify-font-values/src/lib/minify-family.js"
                keywords_js: str = "node_modules/postcss-minify-font-values/src/lib/keywords.js"
            lib = _node_modules_postcss_minify_font_values_src_lib()
        src = _node_modules_postcss_minify_font_values_src()
    postcss_minify_font_values = _node_modules_postcss_minify_font_values()

    class _node_modules_postcss_unique_selectors:
        src: str = "node_modules/postcss-unique-selectors/src/index.js"
    postcss_unique_selectors = _node_modules_postcss_unique_selectors()

    class _node_modules_signal_exit:

        class _node_modules_signal_exit_dist:

            class _node_modules_signal_exit_dist_mjs:
                index_js: str = "node_modules/signal-exit/dist/mjs/index.js"
                browser_js: str = "node_modules/signal-exit/dist/mjs/browser.js"
                signals_js: str = "node_modules/signal-exit/dist/mjs/signals.js"
            mjs = _node_modules_signal_exit_dist_mjs()

            class _node_modules_signal_exit_dist_cjs:
                index_js: str = "node_modules/signal-exit/dist/cjs/index.js"
                browser_js: str = "node_modules/signal-exit/dist/cjs/browser.js"
                signals_js: str = "node_modules/signal-exit/dist/cjs/signals.js"
            cjs = _node_modules_signal_exit_dist_cjs()
        dist = _node_modules_signal_exit_dist()
    signal_exit = _node_modules_signal_exit()

    class _node_modules_eventemitter3:
        index_js: str = "node_modules/eventemitter3/index.js"

        class _node_modules_eventemitter3_umd:
            eventemitter3_min_js: str = "node_modules/eventemitter3/umd/eventemitter3.min.js"
            eventemitter3_js: str = "node_modules/eventemitter3/umd/eventemitter3.js"
        umd = _node_modules_eventemitter3_umd()
    eventemitter3 = _node_modules_eventemitter3()

    class _node_modules_nodelib:

        class _node_modules_nodelib_fs_scandir:

            class _node_modules_nodelib_fs_scandir_out:
                constants_js: str = "node_modules/@nodelib/fs.scandir/out/constants.js"
                settings_js: str = "node_modules/@nodelib/fs.scandir/out/settings.js"
                index_js: str = "node_modules/@nodelib/fs.scandir/out/index.js"

                class _node_modules_nodelib_fs_scandir_out_utils:
                    fs_js: str = "node_modules/@nodelib/fs.scandir/out/utils/fs.js"
                    index_js: str = "node_modules/@nodelib/fs.scandir/out/utils/index.js"
                utils = _node_modules_nodelib_fs_scandir_out_utils()
                adapters: str = "node_modules/@nodelib/fs.scandir/out/adapters/fs.js"

                class _node_modules_nodelib_fs_scandir_out_providers:
                    async_js: str = "node_modules/@nodelib/fs.scandir/out/providers/async.js"
                    common_js: str = "node_modules/@nodelib/fs.scandir/out/providers/common.js"
                    sync_js: str = "node_modules/@nodelib/fs.scandir/out/providers/sync.js"
                providers = _node_modules_nodelib_fs_scandir_out_providers()
                types: str = "node_modules/@nodelib/fs.scandir/out/types/index.js"
            out = _node_modules_nodelib_fs_scandir_out()
        fs_scandir = _node_modules_nodelib_fs_scandir()

        class _node_modules_nodelib_fs_walk:

            class _node_modules_nodelib_fs_walk_out:
                settings_js: str = "node_modules/@nodelib/fs.walk/out/settings.js"
                index_js: str = "node_modules/@nodelib/fs.walk/out/index.js"

                class _node_modules_nodelib_fs_walk_out_readers:
                    async_js: str = "node_modules/@nodelib/fs.walk/out/readers/async.js"
                    reader_js: str = "node_modules/@nodelib/fs.walk/out/readers/reader.js"
                    common_js: str = "node_modules/@nodelib/fs.walk/out/readers/common.js"
                    sync_js: str = "node_modules/@nodelib/fs.walk/out/readers/sync.js"
                readers = _node_modules_nodelib_fs_walk_out_readers()

                class _node_modules_nodelib_fs_walk_out_providers:
                    async_js: str = "node_modules/@nodelib/fs.walk/out/providers/async.js"
                    index_js: str = "node_modules/@nodelib/fs.walk/out/providers/index.js"
                    stream_js: str = "node_modules/@nodelib/fs.walk/out/providers/stream.js"
                    sync_js: str = "node_modules/@nodelib/fs.walk/out/providers/sync.js"
                providers = _node_modules_nodelib_fs_walk_out_providers()
                types: str = "node_modules/@nodelib/fs.walk/out/types/index.js"
            out = _node_modules_nodelib_fs_walk_out()
        fs_walk = _node_modules_nodelib_fs_walk()

        class _node_modules_nodelib_fs_stat:

            class _node_modules_nodelib_fs_stat_out:
                settings_js: str = "node_modules/@nodelib/fs.stat/out/settings.js"
                index_js: str = "node_modules/@nodelib/fs.stat/out/index.js"
                adapters: str = "node_modules/@nodelib/fs.stat/out/adapters/fs.js"

                class _node_modules_nodelib_fs_stat_out_providers:
                    async_js: str = "node_modules/@nodelib/fs.stat/out/providers/async.js"
                    sync_js: str = "node_modules/@nodelib/fs.stat/out/providers/sync.js"
                providers = _node_modules_nodelib_fs_stat_out_providers()
                types: str = "node_modules/@nodelib/fs.stat/out/types/index.js"
            out = _node_modules_nodelib_fs_stat_out()
        fs_stat = _node_modules_nodelib_fs_stat()
    nodelib = _node_modules_nodelib()

    class _node_modules_rollup:

        class _node_modules_rollup_dist:
            rollup_js: str = "node_modules/rollup/dist/rollup.js"
            getLogFilter_js: str = "node_modules/rollup/dist/getLogFilter.js"
            parseAst_js: str = "node_modules/rollup/dist/parseAst.js"
            native_js: str = "node_modules/rollup/dist/native.js"
            loadConfigFile_js: str = "node_modules/rollup/dist/loadConfigFile.js"

            class _node_modules_rollup_dist_es:
                rollup_js: str = "node_modules/rollup/dist/es/rollup.js"
                getLogFilter_js: str = "node_modules/rollup/dist/es/getLogFilter.js"
                parseAst_js: str = "node_modules/rollup/dist/es/parseAst.js"

                class _node_modules_rollup_dist_es_shared:
                    watch_js: str = "node_modules/rollup/dist/es/shared/watch.js"
                    node_entry_js: str = "node_modules/rollup/dist/es/shared/node-entry.js"
                    parseAst_js: str = "node_modules/rollup/dist/es/shared/parseAst.js"
                shared = _node_modules_rollup_dist_es_shared()
            es = _node_modules_rollup_dist_es()

            class _node_modules_rollup_dist_shared:
                rollup_js: str = "node_modules/rollup/dist/shared/rollup.js"
                watch_js: str = "node_modules/rollup/dist/shared/watch.js"
                watch_cli_js: str = "node_modules/rollup/dist/shared/watch-cli.js"
                fsevents_importer_js: str = "node_modules/rollup/dist/shared/fsevents-importer.js"
                index_js: str = "node_modules/rollup/dist/shared/index.js"
                parseAst_js: str = "node_modules/rollup/dist/shared/parseAst.js"
                loadConfigFile_js: str = "node_modules/rollup/dist/shared/loadConfigFile.js"
            shared = _node_modules_rollup_dist_shared()
        dist = _node_modules_rollup_dist()
    rollup = _node_modules_rollup()

    class _node_modules_brace_expansion:
        index_js: str = "node_modules/brace-expansion/index.js"
    brace_expansion = _node_modules_brace_expansion()

    class _node_modules_cssnano_preset_default:
        src: str = "node_modules/cssnano-preset-default/src/index.js"
    cssnano_preset_default = _node_modules_cssnano_preset_default()

    class _node_modules_domelementtype:

        class _node_modules_domelementtype_lib:
            index_js: str = "node_modules/domelementtype/lib/index.js"
            esm: str = "node_modules/domelementtype/lib/esm/index.js"
        lib = _node_modules_domelementtype_lib()
    domelementtype = _node_modules_domelementtype()
    ansi_regex: str = "node_modules/ansi-regex/index.js"

    class _node_modules_jridgewell:

        class _node_modules_jridgewell_resolve_uri:

            class _node_modules_jridgewell_resolve_uri_dist:
                resolve_uri_umd_js: str = "node_modules/@jridgewell/resolve-uri/dist/resolve-uri.umd.js"
            dist = _node_modules_jridgewell_resolve_uri_dist()
        resolve_uri = _node_modules_jridgewell_resolve_uri()

        class _node_modules_jridgewell_set_array:

            class _node_modules_jridgewell_set_array_dist:
                set_array_umd_js: str = "node_modules/@jridgewell/set-array/dist/set-array.umd.js"
            dist = _node_modules_jridgewell_set_array_dist()
        set_array = _node_modules_jridgewell_set_array()

        class _node_modules_jridgewell_source_map:

            class _node_modules_jridgewell_source_map_dist:
                source_map_umd_js: str = "node_modules/@jridgewell/source-map/dist/source-map.umd.js"
            dist = _node_modules_jridgewell_source_map_dist()
        source_map = _node_modules_jridgewell_source_map()

        class _node_modules_jridgewell_gen_mapping:

            class _node_modules_jridgewell_gen_mapping_dist:
                gen_mapping_umd_js: str = "node_modules/@jridgewell/gen-mapping/dist/gen-mapping.umd.js"
            dist = _node_modules_jridgewell_gen_mapping_dist()
        gen_mapping = _node_modules_jridgewell_gen_mapping()

        class _node_modules_jridgewell_sourcemap_codec:

            class _node_modules_jridgewell_sourcemap_codec_dist:
                sourcemap_codec_umd_js: str = "node_modules/@jridgewell/sourcemap-codec/dist/sourcemap-codec.umd.js"
            dist = _node_modules_jridgewell_sourcemap_codec_dist()
        sourcemap_codec = _node_modules_jridgewell_sourcemap_codec()

        class _node_modules_jridgewell_trace_mapping:

            class _node_modules_jridgewell_trace_mapping_dist:
                trace_mapping_umd_js: str = "node_modules/@jridgewell/trace-mapping/dist/trace-mapping.umd.js"
            dist = _node_modules_jridgewell_trace_mapping_dist()
        trace_mapping = _node_modules_jridgewell_trace_mapping()
    jridgewell = _node_modules_jridgewell()
    readdirp: str = "node_modules/readdirp/index.js"

    class _node_modules_postcss_js:
        async_js: str = "node_modules/postcss-js/async.js"
        parser_js: str = "node_modules/postcss-js/parser.js"
        process_result_js: str = "node_modules/postcss-js/process-result.js"
        index_js: str = "node_modules/postcss-js/index.js"
        objectifier_js: str = "node_modules/postcss-js/objectifier.js"
        sync_js: str = "node_modules/postcss-js/sync.js"
    postcss_js = _node_modules_postcss_js()

    class _node_modules_postcss_discard_duplicates:
        src: str = "node_modules/postcss-discard-duplicates/src/index.js"
    postcss_discard_duplicates = _node_modules_postcss_discard_duplicates()
    color_name: str = "node_modules/color-name/index.js"
    path_key: str = "node_modules/path-key/index.js"

    class _node_modules_yaml:
        seq_js: str = "node_modules/yaml/seq.js"
        schema_js: str = "node_modules/yaml/schema.js"
        pair_js: str = "node_modules/yaml/pair.js"
        map_js: str = "node_modules/yaml/map.js"
        index_js: str = "node_modules/yaml/index.js"
        util_js: str = "node_modules/yaml/util.js"
        parse_cst_js: str = "node_modules/yaml/parse-cst.js"
        types_js: str = "node_modules/yaml/types.js"
        scalar_js: str = "node_modules/yaml/scalar.js"

        class _node_modules_yaml_browser:
            seq_js: str = "node_modules/yaml/browser/seq.js"
            schema_js: str = "node_modules/yaml/browser/schema.js"
            pair_js: str = "node_modules/yaml/browser/pair.js"
            map_js: str = "node_modules/yaml/browser/map.js"
            index_js: str = "node_modules/yaml/browser/index.js"
            util_js: str = "node_modules/yaml/browser/util.js"
            parse_cst_js: str = "node_modules/yaml/browser/parse-cst.js"
            types_js: str = "node_modules/yaml/browser/types.js"
            scalar_js: str = "node_modules/yaml/browser/scalar.js"

            class _node_modules_yaml_browser_dist:
                resolveSeq_492ab440_js: str = "node_modules/yaml/browser/dist/resolveSeq-492ab440.js"
                PlainValue_b8036b75_js: str = "node_modules/yaml/browser/dist/PlainValue-b8036b75.js"
                warnings_df54cb69_js: str = "node_modules/yaml/browser/dist/warnings-df54cb69.js"
                index_js: str = "node_modules/yaml/browser/dist/index.js"
                util_js: str = "node_modules/yaml/browser/dist/util.js"
                parse_cst_js: str = "node_modules/yaml/browser/dist/parse-cst.js"
                Schema_e94716c8_js: str = "node_modules/yaml/browser/dist/Schema-e94716c8.js"
                types_js: str = "node_modules/yaml/browser/dist/types.js"
                legacy_exports_js: str = "node_modules/yaml/browser/dist/legacy-exports.js"
            dist = _node_modules_yaml_browser_dist()

            class _node_modules_yaml_browser_types:
                omap_js: str = "node_modules/yaml/browser/types/omap.js"
                set_js: str = "node_modules/yaml/browser/types/set.js"
                binary_js: str = "node_modules/yaml/browser/types/binary.js"
                pairs_js: str = "node_modules/yaml/browser/types/pairs.js"
                timestamp_js: str = "node_modules/yaml/browser/types/timestamp.js"
            types = _node_modules_yaml_browser_types()
        browser = _node_modules_yaml_browser()

        class _node_modules_yaml_dist:
            Document_9b4560a1_js: str = "node_modules/yaml/dist/Document-9b4560a1.js"
            resolveSeq_d03cb037_js: str = "node_modules/yaml/dist/resolveSeq-d03cb037.js"
            warnings_1000a372_js: str = "node_modules/yaml/dist/warnings-1000a372.js"
            test_events_js: str = "node_modules/yaml/dist/test-events.js"
            index_js: str = "node_modules/yaml/dist/index.js"
            util_js: str = "node_modules/yaml/dist/util.js"
            parse_cst_js: str = "node_modules/yaml/dist/parse-cst.js"
            PlainValue_ec8e588e_js: str = "node_modules/yaml/dist/PlainValue-ec8e588e.js"
            Schema_88e323a7_js: str = "node_modules/yaml/dist/Schema-88e323a7.js"
            types_js: str = "node_modules/yaml/dist/types.js"
            legacy_exports_js: str = "node_modules/yaml/dist/legacy-exports.js"
        dist = _node_modules_yaml_dist()

        class _node_modules_yaml_types:
            omap_js: str = "node_modules/yaml/types/omap.js"
            set_js: str = "node_modules/yaml/types/set.js"
            binary_js: str = "node_modules/yaml/types/binary.js"
            pairs_js: str = "node_modules/yaml/types/pairs.js"
            timestamp_js: str = "node_modules/yaml/types/timestamp.js"
        types = _node_modules_yaml_types()
    yaml = _node_modules_yaml()

    class _node_modules_postcss_modules_scope:
        src: str = "node_modules/postcss-modules-scope/src/index.js"
    postcss_modules_scope = _node_modules_postcss_modules_scope()

    class _node_modules_builtin_modules:
        index_js: str = "node_modules/builtin-modules/index.js"
        static_js: str = "node_modules/builtin-modules/static.js"
    builtin_modules = _node_modules_builtin_modules()

    class _node_modules_postcss_load_config:

        class _node_modules_postcss_load_config_src:
            index_js: str = "node_modules/postcss-load-config/src/index.js"
            options_js: str = "node_modules/postcss-load-config/src/options.js"
            plugins_js: str = "node_modules/postcss-load-config/src/plugins.js"
            req_js: str = "node_modules/postcss-load-config/src/req.js"
        src = _node_modules_postcss_load_config_src()
    postcss_load_config = _node_modules_postcss_load_config()

    class _node_modules_sucrase:

        class _node_modules_sucrase_node_modules:

            class _node_modules_sucrase_node_modules_commander:
                index_js: str = "node_modules/sucrase/node_modules/commander/index.js"
            commander = _node_modules_sucrase_node_modules_commander()
        node_modules = _node_modules_sucrase_node_modules()

        class _node_modules_sucrase_dist:
            computeSourceMap_js: str = "node_modules/sucrase/dist/computeSourceMap.js"
            cli_js: str = "node_modules/sucrase/dist/cli.js"
            identifyShadowedGlobals_js: str = "node_modules/sucrase/dist/identifyShadowedGlobals.js"
            HelperManager_js: str = "node_modules/sucrase/dist/HelperManager.js"
            NameManager_js: str = "node_modules/sucrase/dist/NameManager.js"
            CJSImportProcessor_js: str = "node_modules/sucrase/dist/CJSImportProcessor.js"
            index_js: str = "node_modules/sucrase/dist/index.js"
            register_js: str = "node_modules/sucrase/dist/register.js"
            Options_gen_types_js: str = "node_modules/sucrase/dist/Options-gen-types.js"
            Options_js: str = "node_modules/sucrase/dist/Options.js"
            TokenProcessor_js: str = "node_modules/sucrase/dist/TokenProcessor.js"

            class _node_modules_sucrase_dist_util:
                shouldElideDefaultExport_js: str = "node_modules/sucrase/dist/util/shouldElideDefaultExport.js"
                isIdentifier_js: str = "node_modules/sucrase/dist/util/isIdentifier.js"
                getTSImportedNames_js: str = "node_modules/sucrase/dist/util/getTSImportedNames.js"
                getIdentifierNames_js: str = "node_modules/sucrase/dist/util/getIdentifierNames.js"
                getImportExportSpecifierInfo_js: str = "node_modules/sucrase/dist/util/getImportExportSpecifierInfo.js"
                elideImportEquals_js: str = "node_modules/sucrase/dist/util/elideImportEquals.js"
                isExportFrom_js: str = "node_modules/sucrase/dist/util/isExportFrom.js"
                getDeclarationInfo_js: str = "node_modules/sucrase/dist/util/getDeclarationInfo.js"
                getJSXPragmaInfo_js: str = "node_modules/sucrase/dist/util/getJSXPragmaInfo.js"
                formatTokens_js: str = "node_modules/sucrase/dist/util/formatTokens.js"
                getClassInfo_js: str = "node_modules/sucrase/dist/util/getClassInfo.js"
                getNonTypeIdentifiers_js: str = "node_modules/sucrase/dist/util/getNonTypeIdentifiers.js"
                removeMaybeImportAttributes_js: str = "node_modules/sucrase/dist/util/removeMaybeImportAttributes.js"
                isAsyncOperation_js: str = "node_modules/sucrase/dist/util/isAsyncOperation.js"
            util = _node_modules_sucrase_dist_util()

            class _node_modules_sucrase_dist_esm:
                computeSourceMap_js: str = "node_modules/sucrase/dist/esm/computeSourceMap.js"
                cli_js: str = "node_modules/sucrase/dist/esm/cli.js"
                identifyShadowedGlobals_js: str = "node_modules/sucrase/dist/esm/identifyShadowedGlobals.js"
                HelperManager_js: str = "node_modules/sucrase/dist/esm/HelperManager.js"
                NameManager_js: str = "node_modules/sucrase/dist/esm/NameManager.js"
                CJSImportProcessor_js: str = "node_modules/sucrase/dist/esm/CJSImportProcessor.js"
                index_js: str = "node_modules/sucrase/dist/esm/index.js"
                register_js: str = "node_modules/sucrase/dist/esm/register.js"
                Options_gen_types_js: str = "node_modules/sucrase/dist/esm/Options-gen-types.js"
                Options_js: str = "node_modules/sucrase/dist/esm/Options.js"
                TokenProcessor_js: str = "node_modules/sucrase/dist/esm/TokenProcessor.js"

                class _node_modules_sucrase_dist_esm_util:
                    shouldElideDefaultExport_js: str = "node_modules/sucrase/dist/esm/util/shouldElideDefaultExport.js"
                    isIdentifier_js: str = "node_modules/sucrase/dist/esm/util/isIdentifier.js"
                    getTSImportedNames_js: str = "node_modules/sucrase/dist/esm/util/getTSImportedNames.js"
                    getIdentifierNames_js: str = "node_modules/sucrase/dist/esm/util/getIdentifierNames.js"
                    getImportExportSpecifierInfo_js: str = "node_modules/sucrase/dist/esm/util/getImportExportSpecifierInfo.js"
                    elideImportEquals_js: str = "node_modules/sucrase/dist/esm/util/elideImportEquals.js"
                    isExportFrom_js: str = "node_modules/sucrase/dist/esm/util/isExportFrom.js"
                    getDeclarationInfo_js: str = "node_modules/sucrase/dist/esm/util/getDeclarationInfo.js"
                    getJSXPragmaInfo_js: str = "node_modules/sucrase/dist/esm/util/getJSXPragmaInfo.js"
                    formatTokens_js: str = "node_modules/sucrase/dist/esm/util/formatTokens.js"
                    getClassInfo_js: str = "node_modules/sucrase/dist/esm/util/getClassInfo.js"
                    getNonTypeIdentifiers_js: str = "node_modules/sucrase/dist/esm/util/getNonTypeIdentifiers.js"
                    removeMaybeImportAttributes_js: str = "node_modules/sucrase/dist/esm/util/removeMaybeImportAttributes.js"
                    isAsyncOperation_js: str = "node_modules/sucrase/dist/esm/util/isAsyncOperation.js"
                util = _node_modules_sucrase_dist_esm_util()

                class _node_modules_sucrase_dist_esm_parser:
                    index_js: str = "node_modules/sucrase/dist/esm/parser/index.js"

                    class _node_modules_sucrase_dist_esm_parser_util:
                        charcodes_js: str = "node_modules/sucrase/dist/esm/parser/util/charcodes.js"
                        whitespace_js: str = "node_modules/sucrase/dist/esm/parser/util/whitespace.js"
                        identifier_js: str = "node_modules/sucrase/dist/esm/parser/util/identifier.js"
                    util = _node_modules_sucrase_dist_esm_parser_util()

                    class _node_modules_sucrase_dist_esm_parser_plugins:
                        typescript_js: str = "node_modules/sucrase/dist/esm/parser/plugins/typescript.js"
                        flow_js: str = "node_modules/sucrase/dist/esm/parser/plugins/flow.js"
                        types_js: str = "node_modules/sucrase/dist/esm/parser/plugins/types.js"

                        class _node_modules_sucrase_dist_esm_parser_plugins_jsx:
                            index_js: str = "node_modules/sucrase/dist/esm/parser/plugins/jsx/index.js"
                            xhtml_js: str = "node_modules/sucrase/dist/esm/parser/plugins/jsx/xhtml.js"
                        jsx = _node_modules_sucrase_dist_esm_parser_plugins_jsx()
                    plugins = _node_modules_sucrase_dist_esm_parser_plugins()

                    class _node_modules_sucrase_dist_esm_parser_tokenizer:
                        readWordTree_js: str = "node_modules/sucrase/dist/esm/parser/tokenizer/readWordTree.js"
                        index_js: str = "node_modules/sucrase/dist/esm/parser/tokenizer/index.js"
                        keywords_js: str = "node_modules/sucrase/dist/esm/parser/tokenizer/keywords.js"
                        types_js: str = "node_modules/sucrase/dist/esm/parser/tokenizer/types.js"
                        state_js: str = "node_modules/sucrase/dist/esm/parser/tokenizer/state.js"
                        readWord_js: str = "node_modules/sucrase/dist/esm/parser/tokenizer/readWord.js"
                    tokenizer = _node_modules_sucrase_dist_esm_parser_tokenizer()

                    class _node_modules_sucrase_dist_esm_parser_traverser:
                        expression_js: str = "node_modules/sucrase/dist/esm/parser/traverser/expression.js"
                        base_js: str = "node_modules/sucrase/dist/esm/parser/traverser/base.js"
                        index_js: str = "node_modules/sucrase/dist/esm/parser/traverser/index.js"
                        util_js: str = "node_modules/sucrase/dist/esm/parser/traverser/util.js"
                        statement_js: str = "node_modules/sucrase/dist/esm/parser/traverser/statement.js"
                        lval_js: str = "node_modules/sucrase/dist/esm/parser/traverser/lval.js"
                    traverser = _node_modules_sucrase_dist_esm_parser_traverser()
                parser = _node_modules_sucrase_dist_esm_parser()

                class _node_modules_sucrase_dist_esm_transformers:
                    Transformer_js: str = "node_modules/sucrase/dist/esm/transformers/Transformer.js"
                    JestHoistTransformer_js: str = "node_modules/sucrase/dist/esm/transformers/JestHoistTransformer.js"
                    OptionalCatchBindingTransformer_js: str = "node_modules/sucrase/dist/esm/transformers/OptionalCatchBindingTransformer.js"
                    RootTransformer_js: str = "node_modules/sucrase/dist/esm/transformers/RootTransformer.js"
                    ESMImportTransformer_js: str = "node_modules/sucrase/dist/esm/transformers/ESMImportTransformer.js"
                    ReactDisplayNameTransformer_js: str = "node_modules/sucrase/dist/esm/transformers/ReactDisplayNameTransformer.js"
                    ReactHotLoaderTransformer_js: str = "node_modules/sucrase/dist/esm/transformers/ReactHotLoaderTransformer.js"
                    OptionalChainingNullishTransformer_js: str = "node_modules/sucrase/dist/esm/transformers/OptionalChainingNullishTransformer.js"
                    TypeScriptTransformer_js: str = "node_modules/sucrase/dist/esm/transformers/TypeScriptTransformer.js"
                    NumericSeparatorTransformer_js: str = "node_modules/sucrase/dist/esm/transformers/NumericSeparatorTransformer.js"
                    JSXTransformer_js: str = "node_modules/sucrase/dist/esm/transformers/JSXTransformer.js"
                    FlowTransformer_js: str = "node_modules/sucrase/dist/esm/transformers/FlowTransformer.js"
                    CJSImportTransformer_js: str = "node_modules/sucrase/dist/esm/transformers/CJSImportTransformer.js"
                transformers = _node_modules_sucrase_dist_esm_transformers()
            esm = _node_modules_sucrase_dist_esm()

            class _node_modules_sucrase_dist_parser:
                index_js: str = "node_modules/sucrase/dist/parser/index.js"

                class _node_modules_sucrase_dist_parser_util:
                    charcodes_js: str = "node_modules/sucrase/dist/parser/util/charcodes.js"
                    whitespace_js: str = "node_modules/sucrase/dist/parser/util/whitespace.js"
                    identifier_js: str = "node_modules/sucrase/dist/parser/util/identifier.js"
                util = _node_modules_sucrase_dist_parser_util()

                class _node_modules_sucrase_dist_parser_plugins:
                    typescript_js: str = "node_modules/sucrase/dist/parser/plugins/typescript.js"
                    flow_js: str = "node_modules/sucrase/dist/parser/plugins/flow.js"
                    types_js: str = "node_modules/sucrase/dist/parser/plugins/types.js"

                    class _node_modules_sucrase_dist_parser_plugins_jsx:
                        index_js: str = "node_modules/sucrase/dist/parser/plugins/jsx/index.js"
                        xhtml_js: str = "node_modules/sucrase/dist/parser/plugins/jsx/xhtml.js"
                    jsx = _node_modules_sucrase_dist_parser_plugins_jsx()
                plugins = _node_modules_sucrase_dist_parser_plugins()

                class _node_modules_sucrase_dist_parser_tokenizer:
                    readWordTree_js: str = "node_modules/sucrase/dist/parser/tokenizer/readWordTree.js"
                    index_js: str = "node_modules/sucrase/dist/parser/tokenizer/index.js"
                    keywords_js: str = "node_modules/sucrase/dist/parser/tokenizer/keywords.js"
                    types_js: str = "node_modules/sucrase/dist/parser/tokenizer/types.js"
                    state_js: str = "node_modules/sucrase/dist/parser/tokenizer/state.js"
                    readWord_js: str = "node_modules/sucrase/dist/parser/tokenizer/readWord.js"
                tokenizer = _node_modules_sucrase_dist_parser_tokenizer()

                class _node_modules_sucrase_dist_parser_traverser:
                    expression_js: str = "node_modules/sucrase/dist/parser/traverser/expression.js"
                    base_js: str = "node_modules/sucrase/dist/parser/traverser/base.js"
                    index_js: str = "node_modules/sucrase/dist/parser/traverser/index.js"
                    util_js: str = "node_modules/sucrase/dist/parser/traverser/util.js"
                    statement_js: str = "node_modules/sucrase/dist/parser/traverser/statement.js"
                    lval_js: str = "node_modules/sucrase/dist/parser/traverser/lval.js"
                traverser = _node_modules_sucrase_dist_parser_traverser()
            parser = _node_modules_sucrase_dist_parser()

            class _node_modules_sucrase_dist_transformers:
                Transformer_js: str = "node_modules/sucrase/dist/transformers/Transformer.js"
                JestHoistTransformer_js: str = "node_modules/sucrase/dist/transformers/JestHoistTransformer.js"
                OptionalCatchBindingTransformer_js: str = "node_modules/sucrase/dist/transformers/OptionalCatchBindingTransformer.js"
                RootTransformer_js: str = "node_modules/sucrase/dist/transformers/RootTransformer.js"
                ESMImportTransformer_js: str = "node_modules/sucrase/dist/transformers/ESMImportTransformer.js"
                ReactDisplayNameTransformer_js: str = "node_modules/sucrase/dist/transformers/ReactDisplayNameTransformer.js"
                ReactHotLoaderTransformer_js: str = "node_modules/sucrase/dist/transformers/ReactHotLoaderTransformer.js"
                OptionalChainingNullishTransformer_js: str = "node_modules/sucrase/dist/transformers/OptionalChainingNullishTransformer.js"
                TypeScriptTransformer_js: str = "node_modules/sucrase/dist/transformers/TypeScriptTransformer.js"
                NumericSeparatorTransformer_js: str = "node_modules/sucrase/dist/transformers/NumericSeparatorTransformer.js"
                JSXTransformer_js: str = "node_modules/sucrase/dist/transformers/JSXTransformer.js"
                FlowTransformer_js: str = "node_modules/sucrase/dist/transformers/FlowTransformer.js"
                CJSImportTransformer_js: str = "node_modules/sucrase/dist/transformers/CJSImportTransformer.js"
            transformers = _node_modules_sucrase_dist_transformers()
        dist = _node_modules_sucrase_dist()

        class _node_modules_sucrase_register:
            js_js: str = "node_modules/sucrase/register/js.js"
            ts_legacy_module_interop_js: str = "node_modules/sucrase/register/ts-legacy-module-interop.js"
            index_js: str = "node_modules/sucrase/register/index.js"
            ts_js: str = "node_modules/sucrase/register/ts.js"
            tsx_js: str = "node_modules/sucrase/register/tsx.js"
            jsx_js: str = "node_modules/sucrase/register/jsx.js"
            tsx_legacy_module_interop_js: str = "node_modules/sucrase/register/tsx-legacy-module-interop.js"
        register = _node_modules_sucrase_register()
        ts_node_plugin: str = "node_modules/sucrase/ts-node-plugin/index.js"
    sucrase = _node_modules_sucrase()

    class _node_modules_postcss_colormin:

        class _node_modules_postcss_colormin_src:
            index_js: str = "node_modules/postcss-colormin/src/index.js"
            minifyColor_js: str = "node_modules/postcss-colormin/src/minifyColor.js"
        src = _node_modules_postcss_colormin_src()
    postcss_colormin = _node_modules_postcss_colormin()

    class _node_modules_postcss_normalize_unicode:
        src: str = "node_modules/postcss-normalize-unicode/src/index.js"
    postcss_normalize_unicode = _node_modules_postcss_normalize_unicode()

    class _node_modules_svgo:

        class _node_modules_svgo_lib:
            svgo_node_js: str = "node_modules/svgo/lib/svgo-node.js"
            parser_js: str = "node_modules/svgo/lib/parser.js"
            style_js: str = "node_modules/svgo/lib/style.js"
            css_tools_js: str = "node_modules/svgo/lib/css-tools.js"
            path_js: str = "node_modules/svgo/lib/path.js"
            stringifier_js: str = "node_modules/svgo/lib/stringifier.js"
            svgo_js: str = "node_modules/svgo/lib/svgo.js"
            xast_js: str = "node_modules/svgo/lib/xast.js"

            class _node_modules_svgo_lib_svgo:
                config_js: str = "node_modules/svgo/lib/svgo/config.js"
                coa_js: str = "node_modules/svgo/lib/svgo/coa.js"
                css_class_list_js: str = "node_modules/svgo/lib/svgo/css-class-list.js"
                css_style_declaration_js: str = "node_modules/svgo/lib/svgo/css-style-declaration.js"
                plugins_js: str = "node_modules/svgo/lib/svgo/plugins.js"
                tools_js: str = "node_modules/svgo/lib/svgo/tools.js"
                css_select_adapter_js: str = "node_modules/svgo/lib/svgo/css-select-adapter.js"
                jsAPI_js: str = "node_modules/svgo/lib/svgo/jsAPI.js"
            svgo = _node_modules_svgo_lib_svgo()
        lib = _node_modules_svgo_lib()
        dist: str = "node_modules/svgo/dist/svgo.browser.js"

        class _node_modules_svgo_plugins:
            reusePaths_js: str = "node_modules/svgo/plugins/reusePaths.js"
            convertShapeToPath_js: str = "node_modules/svgo/plugins/convertShapeToPath.js"
            addClassesToSVGElement_js: str = "node_modules/svgo/plugins/addClassesToSVGElement.js"
            removeEmptyAttrs_js: str = "node_modules/svgo/plugins/removeEmptyAttrs.js"
            removeHiddenElems_js: str = "node_modules/svgo/plugins/removeHiddenElems.js"
            convertTransform_js: str = "node_modules/svgo/plugins/convertTransform.js"
            removeAttrs_js: str = "node_modules/svgo/plugins/removeAttrs.js"
            removeXMLNS_js: str = "node_modules/svgo/plugins/removeXMLNS.js"
            minifyStyles_js: str = "node_modules/svgo/plugins/minifyStyles.js"
            cleanupListOfValues_js: str = "node_modules/svgo/plugins/cleanupListOfValues.js"
            removeTitle_js: str = "node_modules/svgo/plugins/removeTitle.js"
            removeOffCanvasPaths_js: str = "node_modules/svgo/plugins/removeOffCanvasPaths.js"
            removeViewBox_js: str = "node_modules/svgo/plugins/removeViewBox.js"
            removeComments_js: str = "node_modules/svgo/plugins/removeComments.js"
            cleanupAttrs_js: str = "node_modules/svgo/plugins/cleanupAttrs.js"
            removeDoctype_js: str = "node_modules/svgo/plugins/removeDoctype.js"
            removeUnknownsAndDefaults_js: str = "node_modules/svgo/plugins/removeUnknownsAndDefaults.js"
            cleanupEnableBackground_js: str = "node_modules/svgo/plugins/cleanupEnableBackground.js"
            moveGroupAttrsToElems_js: str = "node_modules/svgo/plugins/moveGroupAttrsToElems.js"
            inlineStyles_js: str = "node_modules/svgo/plugins/inlineStyles.js"
            sortDefsChildren_js: str = "node_modules/svgo/plugins/sortDefsChildren.js"
            removeRasterImages_js: str = "node_modules/svgo/plugins/removeRasterImages.js"
            mergePaths_js: str = "node_modules/svgo/plugins/mergePaths.js"
            convertPathData_js: str = "node_modules/svgo/plugins/convertPathData.js"
            convertEllipseToCircle_js: str = "node_modules/svgo/plugins/convertEllipseToCircle.js"
            prefixIds_js: str = "node_modules/svgo/plugins/prefixIds.js"
            moveElemsAttrsToGroup_js: str = "node_modules/svgo/plugins/moveElemsAttrsToGroup.js"
            plugins_js: str = "node_modules/svgo/plugins/plugins.js"
            removeXMLProcInst_js: str = "node_modules/svgo/plugins/removeXMLProcInst.js"
            removeEditorsNSData_js: str = "node_modules/svgo/plugins/removeEditorsNSData.js"
            preset_default_js: str = "node_modules/svgo/plugins/preset-default.js"
            transforms_js: str = "node_modules/svgo/plugins/_transforms.js"
            removeAttributesBySelector_js: str = "node_modules/svgo/plugins/removeAttributesBySelector.js"
            removeScriptElement_js: str = "node_modules/svgo/plugins/removeScriptElement.js"
            removeStyleElement_js: str = "node_modules/svgo/plugins/removeStyleElement.js"
            path_js: str = "node_modules/svgo/plugins/_path.js"
            removeEmptyContainers_js: str = "node_modules/svgo/plugins/removeEmptyContainers.js"
            applyTransforms_js: str = "node_modules/svgo/plugins/_applyTransforms.js"
            removeDimensions_js: str = "node_modules/svgo/plugins/removeDimensions.js"
            removeNonInheritableGroupAttrs_js: str = "node_modules/svgo/plugins/removeNonInheritableGroupAttrs.js"
            collapseGroups_js: str = "node_modules/svgo/plugins/collapseGroups.js"
            convertColors_js: str = "node_modules/svgo/plugins/convertColors.js"
            sortAttrs_js: str = "node_modules/svgo/plugins/sortAttrs.js"
            mergeStyles_js: str = "node_modules/svgo/plugins/mergeStyles.js"
            removeUnusedNS_js: str = "node_modules/svgo/plugins/removeUnusedNS.js"
            removeUselessDefs_js: str = "node_modules/svgo/plugins/removeUselessDefs.js"
            removeMetadata_js: str = "node_modules/svgo/plugins/removeMetadata.js"
            cleanupIDs_js: str = "node_modules/svgo/plugins/cleanupIDs.js"
            removeEmptyText_js: str = "node_modules/svgo/plugins/removeEmptyText.js"
            removeDesc_js: str = "node_modules/svgo/plugins/removeDesc.js"
            removeUselessStrokeAndFill_js: str = "node_modules/svgo/plugins/removeUselessStrokeAndFill.js"
            removeElementsByAttr_js: str = "node_modules/svgo/plugins/removeElementsByAttr.js"
            cleanupNumericValues_js: str = "node_modules/svgo/plugins/cleanupNumericValues.js"
            convertStyleToAttrs_js: str = "node_modules/svgo/plugins/convertStyleToAttrs.js"
            addAttributesToSVGElement_js: str = "node_modules/svgo/plugins/addAttributesToSVGElement.js"
            collections_js: str = "node_modules/svgo/plugins/_collections.js"
        plugins = _node_modules_svgo_plugins()
    svgo = _node_modules_svgo()

    class _node_modules_colord:
        index_js: str = "node_modules/colord/index.js"

        class _node_modules_colord_plugins:
            lab_js: str = "node_modules/colord/plugins/lab.js"
            names_js: str = "node_modules/colord/plugins/names.js"
            minify_js: str = "node_modules/colord/plugins/minify.js"
            cmyk_js: str = "node_modules/colord/plugins/cmyk.js"
            lch_js: str = "node_modules/colord/plugins/lch.js"
            xyz_js: str = "node_modules/colord/plugins/xyz.js"
            mix_js: str = "node_modules/colord/plugins/mix.js"
            harmonies_js: str = "node_modules/colord/plugins/harmonies.js"
            hwb_js: str = "node_modules/colord/plugins/hwb.js"
            a11y_js: str = "node_modules/colord/plugins/a11y.js"
        plugins = _node_modules_colord_plugins()
    colord = _node_modules_colord()

    class _node_modules_mdn_data:
        index_js: str = "node_modules/mdn-data/index.js"
        css: str = "node_modules/mdn-data/css/index.js"
        l10n: str = "node_modules/mdn-data/l10n/index.js"
        api: str = "node_modules/mdn-data/api/index.js"
    mdn_data = _node_modules_mdn_data()

    class _node_modules_lilconfig:
        dist: str = "node_modules/lilconfig/dist/index.js"
    lilconfig = _node_modules_lilconfig()

    class _node_modules_style_inject:

        class _node_modules_style_inject_dist:
            style_inject_js: str = "node_modules/style-inject/dist/style-inject.js"
            style_inject_es_js: str = "node_modules/style-inject/dist/style-inject.es.js"
        dist = _node_modules_style_inject_dist()
    style_inject = _node_modules_style_inject()
    safe_buffer: str = "node_modules/safe-buffer/index.js"

    class _node_modules_hasown:
        index_js: str = "node_modules/hasown/index.js"
    hasown = _node_modules_hasown()
    run_parallel: str = "node_modules/run-parallel/index.js"

    class _node_modules_postcss_modules:

        class _node_modules_postcss_modules_build:
            behaviours_js: str = "node_modules/postcss-modules/build/behaviours.js"
            generateScopedName_js: str = "node_modules/postcss-modules/build/generateScopedName.js"
            index_js: str = "node_modules/postcss-modules/build/index.js"
            saveJSON_js: str = "node_modules/postcss-modules/build/saveJSON.js"
            unquote: str = "node_modules/postcss-modules/build/unquote/index.js"

            class _node_modules_postcss_modules_build_css_loader_core:
                parser_js: str = "node_modules/postcss-modules/build/css-loader-core/parser.js"
                loader_js: str = "node_modules/postcss-modules/build/css-loader-core/loader.js"
            css_loader_core = _node_modules_postcss_modules_build_css_loader_core()
        build = _node_modules_postcss_modules_build()
    postcss_modules = _node_modules_postcss_modules()
    buffer_from: str = "node_modules/buffer-from/index.js"

    class _node_modules_safe_identifier:
        reserved_js: str = "node_modules/safe-identifier/reserved.js"
        index_js: str = "node_modules/safe-identifier/index.js"
    safe_identifier = _node_modules_safe_identifier()
    is_builtin_module: str = "node_modules/is-builtin-module/index.js"

    class _node_modules_postcss_discard_comments:

        class _node_modules_postcss_discard_comments_src:
            index_js: str = "node_modules/postcss-discard-comments/src/index.js"

            class _node_modules_postcss_discard_comments_src_lib:
                commentParser_js: str = "node_modules/postcss-discard-comments/src/lib/commentParser.js"
                commentRemover_js: str = "node_modules/postcss-discard-comments/src/lib/commentRemover.js"
            lib = _node_modules_postcss_discard_comments_src_lib()
        src = _node_modules_postcss_discard_comments_src()
    postcss_discard_comments = _node_modules_postcss_discard_comments()

    class _node_modules_dom_serializer:

        class _node_modules_dom_serializer_lib:
            foreignNames_js: str = "node_modules/dom-serializer/lib/foreignNames.js"
            index_js: str = "node_modules/dom-serializer/lib/index.js"

            class _node_modules_dom_serializer_lib_esm:
                foreignNames_js: str = "node_modules/dom-serializer/lib/esm/foreignNames.js"
                index_js: str = "node_modules/dom-serializer/lib/esm/index.js"
            esm = _node_modules_dom_serializer_lib_esm()
        lib = _node_modules_dom_serializer_lib()
    dom_serializer = _node_modules_dom_serializer()

    class _node_modules_stable:
        stable_min_js: str = "node_modules/stable/stable.min.js"
        stable_js: str = "node_modules/stable/stable.js"
    stable = _node_modules_stable()

    class _node_modules_icss_utils:

        class _node_modules_icss_utils_src:
            index_js: str = "node_modules/icss-utils/src/index.js"
            extractICSS_js: str = "node_modules/icss-utils/src/extractICSS.js"
            replaceSymbols_js: str = "node_modules/icss-utils/src/replaceSymbols.js"
            createICSSRules_js: str = "node_modules/icss-utils/src/createICSSRules.js"
            replaceValueSymbols_js: str = "node_modules/icss-utils/src/replaceValueSymbols.js"
        src = _node_modules_icss_utils_src()
    icss_utils = _node_modules_icss_utils()

    class _node_modules_rollup_plugin_postcss:
        dist: str = "node_modules/rollup-plugin-postcss/dist/index.js"
    rollup_plugin_postcss = _node_modules_rollup_plugin_postcss()

    class _node_modules_randombytes:
        test_js: str = "node_modules/randombytes/test.js"
        index_js: str = "node_modules/randombytes/index.js"
        browser_js: str = "node_modules/randombytes/browser.js"
    randombytes = _node_modules_randombytes()

    class _node_modules_commondir:
        index_js: str = "node_modules/commondir/index.js"
        example: str = "node_modules/commondir/example/dir.js"
        test: str = "node_modules/commondir/test/dirs.js"
    commondir = _node_modules_commondir()

    class _node_modules_minimatch:

        class _node_modules_minimatch_dist:

            class _node_modules_minimatch_dist_esm:
                index_js: str = "node_modules/minimatch/dist/esm/index.js"
                assert_valid_pattern_js: str = "node_modules/minimatch/dist/esm/assert-valid-pattern.js"
                unescape_js: str = "node_modules/minimatch/dist/esm/unescape.js"
                ast_js: str = "node_modules/minimatch/dist/esm/ast.js"
                escape_js: str = "node_modules/minimatch/dist/esm/escape.js"
                brace_expressions_js: str = "node_modules/minimatch/dist/esm/brace-expressions.js"
            esm = _node_modules_minimatch_dist_esm()

            class _node_modules_minimatch_dist_commonjs:
                index_js: str = "node_modules/minimatch/dist/commonjs/index.js"
                assert_valid_pattern_js: str = "node_modules/minimatch/dist/commonjs/assert-valid-pattern.js"
                unescape_js: str = "node_modules/minimatch/dist/commonjs/unescape.js"
                ast_js: str = "node_modules/minimatch/dist/commonjs/ast.js"
                escape_js: str = "node_modules/minimatch/dist/commonjs/escape.js"
                brace_expressions_js: str = "node_modules/minimatch/dist/commonjs/brace-expressions.js"
            commonjs = _node_modules_minimatch_dist_commonjs()
        dist = _node_modules_minimatch_dist()
    minimatch = _node_modules_minimatch()

    class _node_modules_postcss_normalize_whitespace:
        src: str = "node_modules/postcss-normalize-whitespace/src/index.js"
    postcss_normalize_whitespace = _node_modules_postcss_normalize_whitespace()

    class _node_modules_csso:

        class _node_modules_csso_lib:
            index_js: str = "node_modules/csso/lib/index.js"
            compress_js: str = "node_modules/csso/lib/compress.js"
            usage_js: str = "node_modules/csso/lib/usage.js"

            class _node_modules_csso_lib_restructure:
                utils_js: str = "node_modules/csso/lib/restructure/utils.js"
                n_8_restructRuleset_js: str = "node_modules/csso/lib/restructure/8-restructRuleset.js"
                index_js: str = "node_modules/csso/lib/restructure/index.js"
                n_3_disjoinRuleset_js: str = "node_modules/csso/lib/restructure/3-disjoinRuleset.js"
                n_2_initialMergeRuleset_js: str = "node_modules/csso/lib/restructure/2-initialMergeRuleset.js"
                n_1_mergeAtrule_js: str = "node_modules/csso/lib/restructure/1-mergeAtrule.js"
                n_7_mergeRuleset_js: str = "node_modules/csso/lib/restructure/7-mergeRuleset.js"
                n_4_restructShorthand_js: str = "node_modules/csso/lib/restructure/4-restructShorthand.js"
                n_6_restructBlock_js: str = "node_modules/csso/lib/restructure/6-restructBlock.js"

                class _node_modules_csso_lib_restructure_prepare:
                    createDeclarationIndexer_js: str = "node_modules/csso/lib/restructure/prepare/createDeclarationIndexer.js"
                    processSelector_js: str = "node_modules/csso/lib/restructure/prepare/processSelector.js"
                    index_js: str = "node_modules/csso/lib/restructure/prepare/index.js"
                    specificity_js: str = "node_modules/csso/lib/restructure/prepare/specificity.js"
                prepare = _node_modules_csso_lib_restructure_prepare()
            restructure = _node_modules_csso_lib_restructure()

            class _node_modules_csso_lib_clean:
                utils_js: str = "node_modules/csso/lib/clean/utils.js"
                TypeSelector_js: str = "node_modules/csso/lib/clean/TypeSelector.js"
                Raw_js: str = "node_modules/csso/lib/clean/Raw.js"
                index_js: str = "node_modules/csso/lib/clean/index.js"
                Atrule_js: str = "node_modules/csso/lib/clean/Atrule.js"
                Declaration_js: str = "node_modules/csso/lib/clean/Declaration.js"
                Rule_js: str = "node_modules/csso/lib/clean/Rule.js"
                Comment_js: str = "node_modules/csso/lib/clean/Comment.js"
                WhiteSpace_js: str = "node_modules/csso/lib/clean/WhiteSpace.js"
            clean = _node_modules_csso_lib_clean()

            class _node_modules_csso_lib_replace:
                color_js: str = "node_modules/csso/lib/replace/color.js"
                Url_js: str = "node_modules/csso/lib/replace/Url.js"
                Value_js: str = "node_modules/csso/lib/replace/Value.js"
                String_js: str = "node_modules/csso/lib/replace/String.js"
                Number_js: str = "node_modules/csso/lib/replace/Number.js"
                Percentage_js: str = "node_modules/csso/lib/replace/Percentage.js"
                index_js: str = "node_modules/csso/lib/replace/index.js"
                Atrule_js: str = "node_modules/csso/lib/replace/Atrule.js"
                Dimension_js: str = "node_modules/csso/lib/replace/Dimension.js"
                AttributeSelector_js: str = "node_modules/csso/lib/replace/AttributeSelector.js"
                atrule: str = "node_modules/csso/lib/replace/atrule/keyframes.js"

                class _node_modules_csso_lib_replace_property:
                    background_js: str = "node_modules/csso/lib/replace/property/background.js"
                    font_js: str = "node_modules/csso/lib/replace/property/font.js"
                    font_weight_js: str = "node_modules/csso/lib/replace/property/font-weight.js"
                    border_js: str = "node_modules/csso/lib/replace/property/border.js"
                property = _node_modules_csso_lib_replace_property()
            replace = _node_modules_csso_lib_replace()
        lib = _node_modules_csso_lib()

        class _node_modules_csso_dist:
            csso_js: str = "node_modules/csso/dist/csso.js"
            csso_min_js: str = "node_modules/csso/dist/csso.min.js"
        dist = _node_modules_csso_dist()
    csso = _node_modules_csso()
    import_from: str = "node_modules/import-from/index.js"

    class _node_modules_postcss_reduce_transforms:
        src: str = "node_modules/postcss-reduce-transforms/src/index.js"
    postcss_reduce_transforms = _node_modules_postcss_reduce_transforms()

    class _node_modules_path_scurry:

        class _node_modules_path_scurry_dist:
            esm: str = "node_modules/path-scurry/dist/esm/index.js"
            commonjs: str = "node_modules/path-scurry/dist/commonjs/index.js"
        dist = _node_modules_path_scurry_dist()
    path_scurry = _node_modules_path_scurry()

    class _node_modules_domutils:

        class _node_modules_domutils_lib:
            legacy_js: str = "node_modules/domutils/lib/legacy.js"
            index_js: str = "node_modules/domutils/lib/index.js"
            stringify_js: str = "node_modules/domutils/lib/stringify.js"
            querying_js: str = "node_modules/domutils/lib/querying.js"
            helpers_js: str = "node_modules/domutils/lib/helpers.js"
            manipulation_js: str = "node_modules/domutils/lib/manipulation.js"
            feeds_js: str = "node_modules/domutils/lib/feeds.js"
            traversal_js: str = "node_modules/domutils/lib/traversal.js"
        lib = _node_modules_domutils_lib()
    domutils = _node_modules_domutils()

    class _node_modules_any_promise:
        implementation_js: str = "node_modules/any-promise/implementation.js"
        index_js: str = "node_modules/any-promise/index.js"
        register_shim_js: str = "node_modules/any-promise/register-shim.js"
        register_js: str = "node_modules/any-promise/register.js"
        optional_js: str = "node_modules/any-promise/optional.js"
        loader_js: str = "node_modules/any-promise/loader.js"

        class _node_modules_any_promise_register:
            vow_js: str = "node_modules/any-promise/register/vow.js"
            rsvp_js: str = "node_modules/any-promise/register/rsvp.js"
            es6_promise_js: str = "node_modules/any-promise/register/es6-promise.js"
            lie_js: str = "node_modules/any-promise/register/lie.js"
            q_js: str = "node_modules/any-promise/register/q.js"
            bluebird_js: str = "node_modules/any-promise/register/bluebird.js"
            when_js: str = "node_modules/any-promise/register/when.js"
            pinkie_js: str = "node_modules/any-promise/register/pinkie.js"
            native_promise_only_js: str = "node_modules/any-promise/register/native-promise-only.js"
            promise_js: str = "node_modules/any-promise/register/promise.js"
        register = _node_modules_any_promise_register()
    any_promise = _node_modules_any_promise()

    class _node_modules_rollup_pluginutils:

        class _node_modules_rollup_pluginutils_node_modules:

            class _node_modules_rollup_pluginutils_node_modules_estree_walker:
                src: str = "node_modules/rollup-pluginutils/node_modules/estree-walker/src/estree-walker.js"
                dist: str = "node_modules/rollup-pluginutils/node_modules/estree-walker/dist/estree-walker.umd.js"
            estree_walker = _node_modules_rollup_pluginutils_node_modules_estree_walker()
        node_modules = _node_modules_rollup_pluginutils_node_modules()

        class _node_modules_rollup_pluginutils_dist:
            pluginutils_cjs_js: str = "node_modules/rollup-pluginutils/dist/pluginutils.cjs.js"
            pluginutils_es_js: str = "node_modules/rollup-pluginutils/dist/pluginutils.es.js"
        dist = _node_modules_rollup_pluginutils_dist()
    rollup_pluginutils = _node_modules_rollup_pluginutils()
    thenify: str = "node_modules/thenify/index.js"

    class _node_modules_util_deprecate:
        node_js: str = "node_modules/util-deprecate/node.js"
        browser_js: str = "node_modules/util-deprecate/browser.js"
    util_deprecate = _node_modules_util_deprecate()

    class _node_modules_didyoumean:
        didYouMean_1_2_1_js: str = "node_modules/didyoumean/didYouMean-1.2.1.js"
        didYouMean_1_2_1_min_js: str = "node_modules/didyoumean/didYouMean-1.2.1.min.js"
    didyoumean = _node_modules_didyoumean()

    class _node_modules_estree_walker:

        class _node_modules_estree_walker_src:
            async_js: str = "node_modules/estree-walker/src/async.js"
            walker_js: str = "node_modules/estree-walker/src/walker.js"
            index_js: str = "node_modules/estree-walker/src/index.js"
            sync_js: str = "node_modules/estree-walker/src/sync.js"
        src = _node_modules_estree_walker_src()

        class _node_modules_estree_walker_dist:
            esm: str = "node_modules/estree-walker/dist/esm/estree-walker.js"
            umd: str = "node_modules/estree-walker/dist/umd/estree-walker.js"
        dist = _node_modules_estree_walker_dist()
    estree_walker = _node_modules_estree_walker()

    class _node_modules_is_core_module:
        index_js: str = "node_modules/is-core-module/index.js"
        test: str = "node_modules/is-core-module/test/index.js"
    is_core_module = _node_modules_is_core_module()

    class _node_modules_jiti:
        register_js: str = "node_modules/jiti/register.js"
        lib: str = "node_modules/jiti/lib/index.js"

        class _node_modules_jiti_dist:
            jiti_js: str = "node_modules/jiti/dist/jiti.js"
            babel_js: str = "node_modules/jiti/dist/babel.js"
        dist = _node_modules_jiti_dist()
        bin: str = "node_modules/jiti/bin/jiti.js"
    jiti = _node_modules_jiti()

    class _node_modules_icss_replace_symbols:
        lib: str = "node_modules/icss-replace-symbols/lib/index.js"
    icss_replace_symbols = _node_modules_icss_replace_symbols()

    class _node_modules_isaacs:

        class _node_modules_isaacs_cliui:

            class _node_modules_isaacs_cliui_build:
                lib: str = "node_modules/@isaacs/cliui/build/lib/index.js"
            build = _node_modules_isaacs_cliui_build()
        cliui = _node_modules_isaacs_cliui()
    isaacs = _node_modules_isaacs()

    class _node_modules_cssnano:

        class _node_modules_cssnano_src:
            index_js: str = "node_modules/cssnano/src/index.js"
        src = _node_modules_cssnano_src()
    cssnano = _node_modules_cssnano()

    class _node_modules_magic_string:

        class _node_modules_magic_string_dist:
            magic_string_cjs_js: str = "node_modules/magic-string/dist/magic-string.cjs.js"
            magic_string_umd_js: str = "node_modules/magic-string/dist/magic-string.umd.js"
        dist = _node_modules_magic_string_dist()
    magic_string = _node_modules_magic_string()

    class _node_modules_balanced_match:
        index_js: str = "node_modules/balanced-match/index.js"
    balanced_match = _node_modules_balanced_match()

    class _node_modules_jackspeak:

        class _node_modules_jackspeak_dist:

            class _node_modules_jackspeak_dist_esm:
                parse_args_js: str = "node_modules/jackspeak/dist/esm/parse-args.js"
                index_js: str = "node_modules/jackspeak/dist/esm/index.js"
            esm = _node_modules_jackspeak_dist_esm()

            class _node_modules_jackspeak_dist_commonjs:
                parse_args_js: str = "node_modules/jackspeak/dist/commonjs/parse-args.js"
                index_js: str = "node_modules/jackspeak/dist/commonjs/index.js"
            commonjs = _node_modules_jackspeak_dist_commonjs()
        dist = _node_modules_jackspeak_dist()
    jackspeak = _node_modules_jackspeak()
    queue_microtask: str = "node_modules/queue-microtask/index.js"
    fill_range: str = "node_modules/fill-range/index.js"

    class _node_modules_color_convert:
        index_js: str = "node_modules/color-convert/index.js"
        route_js: str = "node_modules/color-convert/route.js"
        conversions_js: str = "node_modules/color-convert/conversions.js"
    color_convert = _node_modules_color_convert()

    class _node_modules_postcss_normalize_url:
        src: str = "node_modules/postcss-normalize-url/src/index.js"
    postcss_normalize_url = _node_modules_postcss_normalize_url()

    class _node_modules_strip_ansi_cjs:
        index_js: str = "node_modules/strip-ansi-cjs/index.js"

        class _node_modules_strip_ansi_cjs_node_modules:
            ansi_regex: str = "node_modules/strip-ansi-cjs/node_modules/ansi-regex/index.js"
        node_modules = _node_modules_strip_ansi_cjs_node_modules()
    strip_ansi_cjs = _node_modules_strip_ansi_cjs()

    class _node_modules_isexe:
        index_js: str = "node_modules/isexe/index.js"
        mode_js: str = "node_modules/isexe/mode.js"
        windows_js: str = "node_modules/isexe/windows.js"
        test: str = "node_modules/isexe/test/basic.js"
    isexe = _node_modules_isexe()

    class _node_modules_acorn:

        class _node_modules_acorn_dist:
            bin_js: str = "node_modules/acorn/dist/bin.js"
            acorn_js: str = "node_modules/acorn/dist/acorn.js"
        dist = _node_modules_acorn_dist()
    acorn = _node_modules_acorn()

    class _node_modules_read_cache:
        index_js: str = "node_modules/read-cache/index.js"

        class _node_modules_read_cache_node_modules:
            pify: str = "node_modules/read-cache/node_modules/pify/index.js"
        node_modules = _node_modules_read_cache_node_modules()
    read_cache = _node_modules_read_cache()

    class _node_modules_css_select:

        class _node_modules_css_select_lib:
            general_js: str = "node_modules/css-select/lib/general.js"
            index_js: str = "node_modules/css-select/lib/index.js"
            sort_js: str = "node_modules/css-select/lib/sort.js"
            attributes_js: str = "node_modules/css-select/lib/attributes.js"
            types_js: str = "node_modules/css-select/lib/types.js"
            compile_js: str = "node_modules/css-select/lib/compile.js"
            procedure_js: str = "node_modules/css-select/lib/procedure.js"

            class _node_modules_css_select_lib_pseudo_selectors:
                pseudos_js: str = "node_modules/css-select/lib/pseudo-selectors/pseudos.js"
                index_js: str = "node_modules/css-select/lib/pseudo-selectors/index.js"
                filters_js: str = "node_modules/css-select/lib/pseudo-selectors/filters.js"
                subselects_js: str = "node_modules/css-select/lib/pseudo-selectors/subselects.js"
                aliases_js: str = "node_modules/css-select/lib/pseudo-selectors/aliases.js"
            pseudo_selectors = _node_modules_css_select_lib_pseudo_selectors()
        lib = _node_modules_css_select_lib()
    css_select = _node_modules_css_select()

    class _node_modules_glob:

        class _node_modules_glob_dist:

            class _node_modules_glob_dist_esm:
                has_magic_js: str = "node_modules/glob/dist/esm/has-magic.js"
                walker_js: str = "node_modules/glob/dist/esm/walker.js"
                index_js: str = "node_modules/glob/dist/esm/index.js"
                glob_js: str = "node_modules/glob/dist/esm/glob.js"
                processor_js: str = "node_modules/glob/dist/esm/processor.js"
                pattern_js: str = "node_modules/glob/dist/esm/pattern.js"
                ignore_js: str = "node_modules/glob/dist/esm/ignore.js"
            esm = _node_modules_glob_dist_esm()

            class _node_modules_glob_dist_commonjs:
                has_magic_js: str = "node_modules/glob/dist/commonjs/has-magic.js"
                walker_js: str = "node_modules/glob/dist/commonjs/walker.js"
                index_js: str = "node_modules/glob/dist/commonjs/index.js"
                glob_js: str = "node_modules/glob/dist/commonjs/glob.js"
                processor_js: str = "node_modules/glob/dist/commonjs/processor.js"
                pattern_js: str = "node_modules/glob/dist/commonjs/pattern.js"
                ignore_js: str = "node_modules/glob/dist/commonjs/ignore.js"
            commonjs = _node_modules_glob_dist_commonjs()
        dist = _node_modules_glob_dist()
    glob = _node_modules_glob()

    class _node_modules_braces:
        index_js: str = "node_modules/braces/index.js"

        class _node_modules_braces_lib:
            constants_js: str = "node_modules/braces/lib/constants.js"
            parse_js: str = "node_modules/braces/lib/parse.js"
            utils_js: str = "node_modules/braces/lib/utils.js"
            expand_js: str = "node_modules/braces/lib/expand.js"
            stringify_js: str = "node_modules/braces/lib/stringify.js"
            compile_js: str = "node_modules/braces/lib/compile.js"
        lib = _node_modules_braces_lib()
    braces = _node_modules_braces()

    class _node_modules_cssesc:
        cssesc_js: str = "node_modules/cssesc/cssesc.js"
    cssesc = _node_modules_cssesc()

    class _node_modules_source_map:
        source_map_js: str = "node_modules/source-map/source-map.js"

        class _node_modules_source_map_lib:
            source_map_generator_js: str = "node_modules/source-map/lib/source-map-generator.js"
            quick_sort_js: str = "node_modules/source-map/lib/quick-sort.js"
            mapping_list_js: str = "node_modules/source-map/lib/mapping-list.js"
            source_node_js: str = "node_modules/source-map/lib/source-node.js"
            util_js: str = "node_modules/source-map/lib/util.js"
            base64_js: str = "node_modules/source-map/lib/base64.js"
            binary_search_js: str = "node_modules/source-map/lib/binary-search.js"
            source_map_consumer_js: str = "node_modules/source-map/lib/source-map-consumer.js"
            array_set_js: str = "node_modules/source-map/lib/array-set.js"
            base64_vlq_js: str = "node_modules/source-map/lib/base64-vlq.js"
        lib = _node_modules_source_map_lib()

        class _node_modules_source_map_dist:
            source_map_min_js: str = "node_modules/source-map/dist/source-map.min.js"
            source_map_debug_js: str = "node_modules/source-map/dist/source-map.debug.js"
            source_map_js: str = "node_modules/source-map/dist/source-map.js"
        dist = _node_modules_source_map_dist()
    source_map = _node_modules_source_map()

    class _node_modules_postcss_normalize_charset:
        src: str = "node_modules/postcss-normalize-charset/src/index.js"
    postcss_normalize_charset = _node_modules_postcss_normalize_charset()

    class _node_modules_foreground_child:

        class _node_modules_foreground_child_dist:

            class _node_modules_foreground_child_dist_esm:
                index_js: str = "node_modules/foreground-child/dist/esm/index.js"
                proxy_signals_js: str = "node_modules/foreground-child/dist/esm/proxy-signals.js"
                watchdog_js: str = "node_modules/foreground-child/dist/esm/watchdog.js"
                all_signals_js: str = "node_modules/foreground-child/dist/esm/all-signals.js"
            esm = _node_modules_foreground_child_dist_esm()

            class _node_modules_foreground_child_dist_commonjs:
                index_js: str = "node_modules/foreground-child/dist/commonjs/index.js"
                proxy_signals_js: str = "node_modules/foreground-child/dist/commonjs/proxy-signals.js"
                watchdog_js: str = "node_modules/foreground-child/dist/commonjs/watchdog.js"
                all_signals_js: str = "node_modules/foreground-child/dist/commonjs/all-signals.js"
            commonjs = _node_modules_foreground_child_dist_commonjs()
        dist = _node_modules_foreground_child_dist()
    foreground_child = _node_modules_foreground_child()

    class _node_modules_postcss_import:
        index_js: str = "node_modules/postcss-import/index.js"

        class _node_modules_postcss_import_lib:
            process_content_js: str = "node_modules/postcss-import/lib/process-content.js"
            join_layer_js: str = "node_modules/postcss-import/lib/join-layer.js"
            resolve_id_js: str = "node_modules/postcss-import/lib/resolve-id.js"
            data_url_js: str = "node_modules/postcss-import/lib/data-url.js"
            join_media_js: str = "node_modules/postcss-import/lib/join-media.js"
            assign_layer_names_js: str = "node_modules/postcss-import/lib/assign-layer-names.js"
            parse_statements_js: str = "node_modules/postcss-import/lib/parse-statements.js"
            load_content_js: str = "node_modules/postcss-import/lib/load-content.js"
        lib = _node_modules_postcss_import_lib()
    postcss_import = _node_modules_postcss_import()

    class _node_modules_lru_cache:

        class _node_modules_lru_cache_dist:

            class _node_modules_lru_cache_dist_esm:
                index_js: str = "node_modules/lru-cache/dist/esm/index.js"
                index_min_js: str = "node_modules/lru-cache/dist/esm/index.min.js"
            esm = _node_modules_lru_cache_dist_esm()

            class _node_modules_lru_cache_dist_commonjs:
                index_js: str = "node_modules/lru-cache/dist/commonjs/index.js"
                index_min_js: str = "node_modules/lru-cache/dist/commonjs/index.min.js"
            commonjs = _node_modules_lru_cache_dist_commonjs()
        dist = _node_modules_lru_cache_dist()
    lru_cache = _node_modules_lru_cache()

    class _node_modules_tailwindcss:
        defaultConfig_js: str = "node_modules/tailwindcss/defaultConfig.js"
        resolveConfig_js: str = "node_modules/tailwindcss/resolveConfig.js"
        defaultTheme_js: str = "node_modules/tailwindcss/defaultTheme.js"
        utilities_css: str = "node_modules/tailwindcss/utilities.css"
        colors_js: str = "node_modules/tailwindcss/colors.js"
        screens_css: str = "node_modules/tailwindcss/screens.css"
        prettier_config_js: str = "node_modules/tailwindcss/prettier.config.js"
        plugin_js: str = "node_modules/tailwindcss/plugin.js"
        variants_css: str = "node_modules/tailwindcss/variants.css"
        loadConfig_js: str = "node_modules/tailwindcss/loadConfig.js"
        tailwind_css: str = "node_modules/tailwindcss/tailwind.css"
        components_css: str = "node_modules/tailwindcss/components.css"
        base_css: str = "node_modules/tailwindcss/base.css"
        peers: str = "node_modules/tailwindcss/peers/index.js"

        class _node_modules_tailwindcss_node_modules:

            class _node_modules_tailwindcss_node_modules_yaml:
                util_js: str = "node_modules/tailwindcss/node_modules/yaml/util.js"

                class _node_modules_tailwindcss_node_modules_yaml_browser:
                    index_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/index.js"

                    class _node_modules_tailwindcss_node_modules_yaml_browser_dist:
                        log_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/log.js"
                        errors_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/errors.js"
                        index_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/index.js"
                        util_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/util.js"
                        visit_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/visit.js"
                        public_api_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/public-api.js"

                        class _node_modules_tailwindcss_node_modules_yaml_browser_dist_compose:
                            resolve_block_scalar_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/resolve-block-scalar.js"
                            util_empty_scalar_position_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/util-empty-scalar-position.js"
                            compose_node_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/compose-node.js"
                            util_contains_newline_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/util-contains-newline.js"
                            resolve_block_map_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/resolve-block-map.js"
                            util_flow_indent_check_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/util-flow-indent-check.js"
                            compose_collection_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/compose-collection.js"
                            resolve_block_seq_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/resolve-block-seq.js"
                            resolve_flow_scalar_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/resolve-flow-scalar.js"
                            compose_scalar_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/compose-scalar.js"
                            resolve_flow_collection_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/resolve-flow-collection.js"
                            util_map_includes_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/util-map-includes.js"
                            compose_doc_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/compose-doc.js"
                            resolve_end_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/resolve-end.js"
                            composer_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/composer.js"
                            resolve_props_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/compose/resolve-props.js"
                        compose = _node_modules_tailwindcss_node_modules_yaml_browser_dist_compose()

                        class _node_modules_tailwindcss_node_modules_yaml_browser_dist_schema:
                            Schema_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/Schema.js"
                            tags_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/tags.js"

                            class _node_modules_tailwindcss_node_modules_yaml_browser_dist_schema_core:
                                schema_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/core/schema.js"
                                float_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/core/float.js"
                                int_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/core/int.js"
                                bool_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/core/bool.js"
                            core = _node_modules_tailwindcss_node_modules_yaml_browser_dist_schema_core()

                            class _node_modules_tailwindcss_node_modules_yaml_browser_dist_schema_common:
                                seq_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/common/seq.js"
                                string_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/common/string.js"
                                map_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/common/map.js"
                                null_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/common/null.js"
                            common = _node_modules_tailwindcss_node_modules_yaml_browser_dist_schema_common()

                            class _node_modules_tailwindcss_node_modules_yaml_browser_dist_schema_yaml_1_1:
                                omap_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/yaml-1.1/omap.js"
                                set_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/yaml-1.1/set.js"
                                schema_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/yaml-1.1/schema.js"
                                binary_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/yaml-1.1/binary.js"
                                pairs_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/yaml-1.1/pairs.js"
                                timestamp_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/yaml-1.1/timestamp.js"
                                float_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/yaml-1.1/float.js"
                                int_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/yaml-1.1/int.js"
                                bool_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/yaml-1.1/bool.js"
                            yaml_1_1 = _node_modules_tailwindcss_node_modules_yaml_browser_dist_schema_yaml_1_1()
                            json: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/schema/json/schema.js"
                        schema = _node_modules_tailwindcss_node_modules_yaml_browser_dist_schema()

                        class _node_modules_tailwindcss_node_modules_yaml_browser_dist_parse:
                            cst_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/parse/cst.js"
                            parser_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/parse/parser.js"
                            line_counter_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/parse/line-counter.js"
                            cst_stringify_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/parse/cst-stringify.js"
                            cst_scalar_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/parse/cst-scalar.js"
                            cst_visit_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/parse/cst-visit.js"
                            lexer_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/parse/lexer.js"
                        parse = _node_modules_tailwindcss_node_modules_yaml_browser_dist_parse()

                        class _node_modules_tailwindcss_node_modules_yaml_browser_dist_doc:
                            directives_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/doc/directives.js"
                            applyReviver_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/doc/applyReviver.js"
                            anchors_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/doc/anchors.js"
                            createNode_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/doc/createNode.js"
                            Document_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/doc/Document.js"
                        doc = _node_modules_tailwindcss_node_modules_yaml_browser_dist_doc()

                        class _node_modules_tailwindcss_node_modules_yaml_browser_dist_nodes:
                            addPairToJSMap_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/nodes/addPairToJSMap.js"
                            YAMLSeq_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/nodes/YAMLSeq.js"
                            Alias_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/nodes/Alias.js"
                            Scalar_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/nodes/Scalar.js"
                            toJS_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/nodes/toJS.js"
                            Pair_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/nodes/Pair.js"
                            identity_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/nodes/identity.js"
                            Collection_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/nodes/Collection.js"
                            YAMLMap_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/nodes/YAMLMap.js"
                            Node_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/nodes/Node.js"
                        nodes = _node_modules_tailwindcss_node_modules_yaml_browser_dist_nodes()

                        class _node_modules_tailwindcss_node_modules_yaml_browser_dist_stringify:
                            stringifyPair_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/stringify/stringifyPair.js"
                            stringifyDocument_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/stringify/stringifyDocument.js"
                            stringifyString_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/stringify/stringifyString.js"
                            stringifyNumber_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/stringify/stringifyNumber.js"
                            stringify_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/stringify/stringify.js"
                            stringifyCollection_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/stringify/stringifyCollection.js"
                            stringifyComment_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/stringify/stringifyComment.js"
                            foldFlowLines_js: str = "node_modules/tailwindcss/node_modules/yaml/browser/dist/stringify/foldFlowLines.js"
                        stringify = _node_modules_tailwindcss_node_modules_yaml_browser_dist_stringify()
                    dist = _node_modules_tailwindcss_node_modules_yaml_browser_dist()
                browser = _node_modules_tailwindcss_node_modules_yaml_browser()

                class _node_modules_tailwindcss_node_modules_yaml_dist:
                    test_events_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/test-events.js"
                    log_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/log.js"
                    errors_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/errors.js"
                    index_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/index.js"
                    util_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/util.js"
                    visit_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/visit.js"
                    public_api_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/public-api.js"

                    class _node_modules_tailwindcss_node_modules_yaml_dist_compose:
                        resolve_block_scalar_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/resolve-block-scalar.js"
                        util_empty_scalar_position_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/util-empty-scalar-position.js"
                        compose_node_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/compose-node.js"
                        util_contains_newline_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/util-contains-newline.js"
                        resolve_block_map_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/resolve-block-map.js"
                        util_flow_indent_check_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/util-flow-indent-check.js"
                        compose_collection_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/compose-collection.js"
                        resolve_block_seq_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/resolve-block-seq.js"
                        resolve_flow_scalar_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/resolve-flow-scalar.js"
                        compose_scalar_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/compose-scalar.js"
                        resolve_flow_collection_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/resolve-flow-collection.js"
                        util_map_includes_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/util-map-includes.js"
                        compose_doc_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/compose-doc.js"
                        resolve_end_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/resolve-end.js"
                        composer_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/composer.js"
                        resolve_props_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/compose/resolve-props.js"
                    compose = _node_modules_tailwindcss_node_modules_yaml_dist_compose()

                    class _node_modules_tailwindcss_node_modules_yaml_dist_schema:
                        Schema_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/Schema.js"
                        tags_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/tags.js"

                        class _node_modules_tailwindcss_node_modules_yaml_dist_schema_core:
                            schema_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/core/schema.js"
                            float_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/core/float.js"
                            int_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/core/int.js"
                            bool_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/core/bool.js"
                        core = _node_modules_tailwindcss_node_modules_yaml_dist_schema_core()

                        class _node_modules_tailwindcss_node_modules_yaml_dist_schema_common:
                            seq_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/common/seq.js"
                            string_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/common/string.js"
                            map_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/common/map.js"
                            null_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/common/null.js"
                        common = _node_modules_tailwindcss_node_modules_yaml_dist_schema_common()

                        class _node_modules_tailwindcss_node_modules_yaml_dist_schema_yaml_1_1:
                            omap_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/yaml-1.1/omap.js"
                            set_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/yaml-1.1/set.js"
                            schema_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/yaml-1.1/schema.js"
                            binary_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/yaml-1.1/binary.js"
                            pairs_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/yaml-1.1/pairs.js"
                            timestamp_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/yaml-1.1/timestamp.js"
                            float_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/yaml-1.1/float.js"
                            int_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/yaml-1.1/int.js"
                            bool_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/yaml-1.1/bool.js"
                        yaml_1_1 = _node_modules_tailwindcss_node_modules_yaml_dist_schema_yaml_1_1()
                        json: str = "node_modules/tailwindcss/node_modules/yaml/dist/schema/json/schema.js"
                    schema = _node_modules_tailwindcss_node_modules_yaml_dist_schema()

                    class _node_modules_tailwindcss_node_modules_yaml_dist_parse:
                        cst_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/parse/cst.js"
                        parser_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/parse/parser.js"
                        line_counter_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/parse/line-counter.js"
                        cst_stringify_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/parse/cst-stringify.js"
                        cst_scalar_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/parse/cst-scalar.js"
                        cst_visit_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/parse/cst-visit.js"
                        lexer_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/parse/lexer.js"
                    parse = _node_modules_tailwindcss_node_modules_yaml_dist_parse()

                    class _node_modules_tailwindcss_node_modules_yaml_dist_doc:
                        directives_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/doc/directives.js"
                        applyReviver_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/doc/applyReviver.js"
                        anchors_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/doc/anchors.js"
                        createNode_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/doc/createNode.js"
                        Document_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/doc/Document.js"
                    doc = _node_modules_tailwindcss_node_modules_yaml_dist_doc()

                    class _node_modules_tailwindcss_node_modules_yaml_dist_nodes:
                        addPairToJSMap_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/nodes/addPairToJSMap.js"
                        YAMLSeq_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/nodes/YAMLSeq.js"
                        Alias_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/nodes/Alias.js"
                        Scalar_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/nodes/Scalar.js"
                        toJS_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/nodes/toJS.js"
                        Pair_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/nodes/Pair.js"
                        identity_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/nodes/identity.js"
                        Collection_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/nodes/Collection.js"
                        YAMLMap_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/nodes/YAMLMap.js"
                        Node_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/nodes/Node.js"
                    nodes = _node_modules_tailwindcss_node_modules_yaml_dist_nodes()

                    class _node_modules_tailwindcss_node_modules_yaml_dist_stringify:
                        stringifyPair_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/stringify/stringifyPair.js"
                        stringifyDocument_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/stringify/stringifyDocument.js"
                        stringifyString_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/stringify/stringifyString.js"
                        stringifyNumber_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/stringify/stringifyNumber.js"
                        stringify_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/stringify/stringify.js"
                        stringifyCollection_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/stringify/stringifyCollection.js"
                        stringifyComment_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/stringify/stringifyComment.js"
                        foldFlowLines_js: str = "node_modules/tailwindcss/node_modules/yaml/dist/stringify/foldFlowLines.js"
                    stringify = _node_modules_tailwindcss_node_modules_yaml_dist_stringify()
                dist = _node_modules_tailwindcss_node_modules_yaml_dist()
            yaml = _node_modules_tailwindcss_node_modules_yaml()

            class _node_modules_tailwindcss_node_modules_postcss_load_config:

                class _node_modules_tailwindcss_node_modules_postcss_load_config_node_modules:

                    class _node_modules_tailwindcss_node_modules_postcss_load_config_node_modules_lilconfig:
                        src: str = "node_modules/tailwindcss/node_modules/postcss-load-config/node_modules/lilconfig/src/index.js"
                    lilconfig = _node_modules_tailwindcss_node_modules_postcss_load_config_node_modules_lilconfig()
                node_modules = _node_modules_tailwindcss_node_modules_postcss_load_config_node_modules()

                class _node_modules_tailwindcss_node_modules_postcss_load_config_src:
                    index_js: str = "node_modules/tailwindcss/node_modules/postcss-load-config/src/index.js"
                    options_js: str = "node_modules/tailwindcss/node_modules/postcss-load-config/src/options.js"
                    plugins_js: str = "node_modules/tailwindcss/node_modules/postcss-load-config/src/plugins.js"
                    req_js: str = "node_modules/tailwindcss/node_modules/postcss-load-config/src/req.js"
                src = _node_modules_tailwindcss_node_modules_postcss_load_config_src()
            postcss_load_config = _node_modules_tailwindcss_node_modules_postcss_load_config()
        node_modules = _node_modules_tailwindcss_node_modules()

        class _node_modules_tailwindcss_src:
            cli_js: str = "node_modules/tailwindcss/src/cli.js"
            processTailwindFeatures_js: str = "node_modules/tailwindcss/src/processTailwindFeatures.js"
            index_js: str = "node_modules/tailwindcss/src/index.js"
            cli_peer_dependencies_js: str = "node_modules/tailwindcss/src/cli-peer-dependencies.js"
            corePlugins_js: str = "node_modules/tailwindcss/src/corePlugins.js"
            featureFlags_js: str = "node_modules/tailwindcss/src/featureFlags.js"
            plugin_js: str = "node_modules/tailwindcss/src/plugin.js"
            corePluginList_js: str = "node_modules/tailwindcss/src/corePluginList.js"

            class _node_modules_tailwindcss_src_util:
                escapeCommas_js: str = "node_modules/tailwindcss/src/util/escapeCommas.js"
                color_js: str = "node_modules/tailwindcss/src/util/color.js"
                cloneDeep_js: str = "node_modules/tailwindcss/src/util/cloneDeep.js"
                isPlainObject_js: str = "node_modules/tailwindcss/src/util/isPlainObject.js"
                colorNames_js: str = "node_modules/tailwindcss/src/util/colorNames.js"
                createUtilityPlugin_js: str = "node_modules/tailwindcss/src/util/createUtilityPlugin.js"
                removeAlphaVariables_js: str = "node_modules/tailwindcss/src/util/removeAlphaVariables.js"
                parseAnimationValue_js: str = "node_modules/tailwindcss/src/util/parseAnimationValue.js"
                escapeClassName_js: str = "node_modules/tailwindcss/src/util/escapeClassName.js"
                normalizeScreens_js: str = "node_modules/tailwindcss/src/util/normalizeScreens.js"
                createPlugin_js: str = "node_modules/tailwindcss/src/util/createPlugin.js"
                parseGlob_js: str = "node_modules/tailwindcss/src/util/parseGlob.js"
                dataTypes_js: str = "node_modules/tailwindcss/src/util/dataTypes.js"
                resolveConfig_js: str = "node_modules/tailwindcss/src/util/resolveConfig.js"
                defaults_js: str = "node_modules/tailwindcss/src/util/defaults.js"
                log_js: str = "node_modules/tailwindcss/src/util/log.js"
                parseObjectStyles_js: str = "node_modules/tailwindcss/src/util/parseObjectStyles.js"
                pseudoElements_js: str = "node_modules/tailwindcss/src/util/pseudoElements.js"
                withAlphaVariable_js: str = "node_modules/tailwindcss/src/util/withAlphaVariable.js"
                applyImportantSelector_js: str = "node_modules/tailwindcss/src/util/applyImportantSelector.js"
                parseDependency_js: str = "node_modules/tailwindcss/src/util/parseDependency.js"
                splitAtTopLevelOnly_js: str = "node_modules/tailwindcss/src/util/splitAtTopLevelOnly.js"
                nameClass_js: str = "node_modules/tailwindcss/src/util/nameClass.js"
                tap_js: str = "node_modules/tailwindcss/src/util/tap.js"
                toColorValue_js: str = "node_modules/tailwindcss/src/util/toColorValue.js"
                pluginUtils_js: str = "node_modules/tailwindcss/src/util/pluginUtils.js"
                toPath_js: str = "node_modules/tailwindcss/src/util/toPath.js"
                flattenColorPalette_js: str = "node_modules/tailwindcss/src/util/flattenColorPalette.js"
                isSyntacticallyValidPropertyValue_js: str = "node_modules/tailwindcss/src/util/isSyntacticallyValidPropertyValue.js"
                resolveConfigPath_js: str = "node_modules/tailwindcss/src/util/resolveConfigPath.js"
                parseBoxShadowValue_js: str = "node_modules/tailwindcss/src/util/parseBoxShadowValue.js"
                buildMediaQuery_js: str = "node_modules/tailwindcss/src/util/buildMediaQuery.js"
                hashConfig_js: str = "node_modules/tailwindcss/src/util/hashConfig.js"
                formatVariantSelector_js: str = "node_modules/tailwindcss/src/util/formatVariantSelector.js"
                cloneNodes_js: str = "node_modules/tailwindcss/src/util/cloneNodes.js"
                bigSign_js: str = "node_modules/tailwindcss/src/util/bigSign.js"
                responsive_js: str = "node_modules/tailwindcss/src/util/responsive.js"
                isKeyframeRule_js: str = "node_modules/tailwindcss/src/util/isKeyframeRule.js"
                validateConfig_js: str = "node_modules/tailwindcss/src/util/validateConfig.js"
                negateValue_js: str = "node_modules/tailwindcss/src/util/negateValue.js"
                normalizeConfig_js: str = "node_modules/tailwindcss/src/util/normalizeConfig.js"
                prefixSelector_js: str = "node_modules/tailwindcss/src/util/prefixSelector.js"
                getAllConfigs_js: str = "node_modules/tailwindcss/src/util/getAllConfigs.js"
                transformThemeValue_js: str = "node_modules/tailwindcss/src/util/transformThemeValue.js"
                validateFormalSyntax_js: str = "node_modules/tailwindcss/src/util/validateFormalSyntax.js"
                configurePlugins_js: str = "node_modules/tailwindcss/src/util/configurePlugins.js"
            util = _node_modules_tailwindcss_src_util()

            class _node_modules_tailwindcss_src_value_parser:
                parse_js: str = "node_modules/tailwindcss/src/value-parser/parse.js"
                walk_js: str = "node_modules/tailwindcss/src/value-parser/walk.js"
                unit_js: str = "node_modules/tailwindcss/src/value-parser/unit.js"
                index_js: str = "node_modules/tailwindcss/src/value-parser/index.js"
                stringify_js: str = "node_modules/tailwindcss/src/value-parser/stringify.js"
            value_parser = _node_modules_tailwindcss_src_value_parser()

            class _node_modules_tailwindcss_src_cli:
                index_js: str = "node_modules/tailwindcss/src/cli/index.js"
                help: str = "node_modules/tailwindcss/src/cli/help/index.js"
                init: str = "node_modules/tailwindcss/src/cli/init/index.js"

                class _node_modules_tailwindcss_src_cli_build:
                    utils_js: str = "node_modules/tailwindcss/src/cli/build/utils.js"
                    watching_js: str = "node_modules/tailwindcss/src/cli/build/watching.js"
                    index_js: str = "node_modules/tailwindcss/src/cli/build/index.js"
                    plugin_js: str = "node_modules/tailwindcss/src/cli/build/plugin.js"
                    deps_js: str = "node_modules/tailwindcss/src/cli/build/deps.js"
                build = _node_modules_tailwindcss_src_cli_build()
            cli = _node_modules_tailwindcss_src_cli()

            class _node_modules_tailwindcss_src_lib:
                defaultExtractor_js: str = "node_modules/tailwindcss/src/lib/defaultExtractor.js"
                regex_js: str = "node_modules/tailwindcss/src/lib/regex.js"
                substituteScreenAtRules_js: str = "node_modules/tailwindcss/src/lib/substituteScreenAtRules.js"
                evaluateTailwindFunctions_js: str = "node_modules/tailwindcss/src/lib/evaluateTailwindFunctions.js"
                expandTailwindAtRules_js: str = "node_modules/tailwindcss/src/lib/expandTailwindAtRules.js"
                normalizeTailwindDirectives_js: str = "node_modules/tailwindcss/src/lib/normalizeTailwindDirectives.js"
                setupTrackingContext_js: str = "node_modules/tailwindcss/src/lib/setupTrackingContext.js"
                content_js: str = "node_modules/tailwindcss/src/lib/content.js"
                sharedState_js: str = "node_modules/tailwindcss/src/lib/sharedState.js"
                getModuleDependencies_js: str = "node_modules/tailwindcss/src/lib/getModuleDependencies.js"
                findAtConfigPath_js: str = "node_modules/tailwindcss/src/lib/findAtConfigPath.js"
                remap_bitfield_js: str = "node_modules/tailwindcss/src/lib/remap-bitfield.js"
                offsets_js: str = "node_modules/tailwindcss/src/lib/offsets.js"
                partitionApplyAtRules_js: str = "node_modules/tailwindcss/src/lib/partitionApplyAtRules.js"
                setupContextUtils_js: str = "node_modules/tailwindcss/src/lib/setupContextUtils.js"
                cacheInvalidation_js: str = "node_modules/tailwindcss/src/lib/cacheInvalidation.js"
                collapseAdjacentRules_js: str = "node_modules/tailwindcss/src/lib/collapseAdjacentRules.js"
                collapseDuplicateDeclarations_js: str = "node_modules/tailwindcss/src/lib/collapseDuplicateDeclarations.js"
                resolveDefaultsAtRules_js: str = "node_modules/tailwindcss/src/lib/resolveDefaultsAtRules.js"
                generateRules_js: str = "node_modules/tailwindcss/src/lib/generateRules.js"
                expandApplyAtRules_js: str = "node_modules/tailwindcss/src/lib/expandApplyAtRules.js"
            lib = _node_modules_tailwindcss_src_lib()
            css: str = "node_modules/tailwindcss/src/css/preflight.css"

            class _node_modules_tailwindcss_src_postcss_plugins:

                class _node_modules_tailwindcss_src_postcss_plugins_nesting:
                    index_js: str = "node_modules/tailwindcss/src/postcss-plugins/nesting/index.js"
                    plugin_js: str = "node_modules/tailwindcss/src/postcss-plugins/nesting/plugin.js"
                nesting = _node_modules_tailwindcss_src_postcss_plugins_nesting()
            postcss_plugins = _node_modules_tailwindcss_src_postcss_plugins()

            class _node_modules_tailwindcss_src_public:
                create_plugin_js: str = "node_modules/tailwindcss/src/public/create-plugin.js"
                load_config_js: str = "node_modules/tailwindcss/src/public/load-config.js"
                colors_js: str = "node_modules/tailwindcss/src/public/colors.js"
                resolve_config_js: str = "node_modules/tailwindcss/src/public/resolve-config.js"
                default_theme_js: str = "node_modules/tailwindcss/src/public/default-theme.js"
                default_config_js: str = "node_modules/tailwindcss/src/public/default-config.js"
            public = _node_modules_tailwindcss_src_public()
        src = _node_modules_tailwindcss_src()

        class _node_modules_tailwindcss_lib:
            cli_js: str = "node_modules/tailwindcss/lib/cli.js"
            processTailwindFeatures_js: str = "node_modules/tailwindcss/lib/processTailwindFeatures.js"
            index_js: str = "node_modules/tailwindcss/lib/index.js"
            cli_peer_dependencies_js: str = "node_modules/tailwindcss/lib/cli-peer-dependencies.js"
            corePlugins_js: str = "node_modules/tailwindcss/lib/corePlugins.js"
            featureFlags_js: str = "node_modules/tailwindcss/lib/featureFlags.js"
            plugin_js: str = "node_modules/tailwindcss/lib/plugin.js"
            corePluginList_js: str = "node_modules/tailwindcss/lib/corePluginList.js"

            class _node_modules_tailwindcss_lib_util:
                escapeCommas_js: str = "node_modules/tailwindcss/lib/util/escapeCommas.js"
                color_js: str = "node_modules/tailwindcss/lib/util/color.js"
                cloneDeep_js: str = "node_modules/tailwindcss/lib/util/cloneDeep.js"
                isPlainObject_js: str = "node_modules/tailwindcss/lib/util/isPlainObject.js"
                colorNames_js: str = "node_modules/tailwindcss/lib/util/colorNames.js"
                createUtilityPlugin_js: str = "node_modules/tailwindcss/lib/util/createUtilityPlugin.js"
                removeAlphaVariables_js: str = "node_modules/tailwindcss/lib/util/removeAlphaVariables.js"
                parseAnimationValue_js: str = "node_modules/tailwindcss/lib/util/parseAnimationValue.js"
                escapeClassName_js: str = "node_modules/tailwindcss/lib/util/escapeClassName.js"
                normalizeScreens_js: str = "node_modules/tailwindcss/lib/util/normalizeScreens.js"
                createPlugin_js: str = "node_modules/tailwindcss/lib/util/createPlugin.js"
                parseGlob_js: str = "node_modules/tailwindcss/lib/util/parseGlob.js"
                dataTypes_js: str = "node_modules/tailwindcss/lib/util/dataTypes.js"
                resolveConfig_js: str = "node_modules/tailwindcss/lib/util/resolveConfig.js"
                defaults_js: str = "node_modules/tailwindcss/lib/util/defaults.js"
                log_js: str = "node_modules/tailwindcss/lib/util/log.js"
                parseObjectStyles_js: str = "node_modules/tailwindcss/lib/util/parseObjectStyles.js"
                pseudoElements_js: str = "node_modules/tailwindcss/lib/util/pseudoElements.js"
                withAlphaVariable_js: str = "node_modules/tailwindcss/lib/util/withAlphaVariable.js"
                applyImportantSelector_js: str = "node_modules/tailwindcss/lib/util/applyImportantSelector.js"
                parseDependency_js: str = "node_modules/tailwindcss/lib/util/parseDependency.js"
                splitAtTopLevelOnly_js: str = "node_modules/tailwindcss/lib/util/splitAtTopLevelOnly.js"
                nameClass_js: str = "node_modules/tailwindcss/lib/util/nameClass.js"
                tap_js: str = "node_modules/tailwindcss/lib/util/tap.js"
                toColorValue_js: str = "node_modules/tailwindcss/lib/util/toColorValue.js"
                pluginUtils_js: str = "node_modules/tailwindcss/lib/util/pluginUtils.js"
                toPath_js: str = "node_modules/tailwindcss/lib/util/toPath.js"
                flattenColorPalette_js: str = "node_modules/tailwindcss/lib/util/flattenColorPalette.js"
                isSyntacticallyValidPropertyValue_js: str = "node_modules/tailwindcss/lib/util/isSyntacticallyValidPropertyValue.js"
                resolveConfigPath_js: str = "node_modules/tailwindcss/lib/util/resolveConfigPath.js"
                parseBoxShadowValue_js: str = "node_modules/tailwindcss/lib/util/parseBoxShadowValue.js"
                buildMediaQuery_js: str = "node_modules/tailwindcss/lib/util/buildMediaQuery.js"
                hashConfig_js: str = "node_modules/tailwindcss/lib/util/hashConfig.js"
                formatVariantSelector_js: str = "node_modules/tailwindcss/lib/util/formatVariantSelector.js"
                cloneNodes_js: str = "node_modules/tailwindcss/lib/util/cloneNodes.js"
                bigSign_js: str = "node_modules/tailwindcss/lib/util/bigSign.js"
                responsive_js: str = "node_modules/tailwindcss/lib/util/responsive.js"
                isKeyframeRule_js: str = "node_modules/tailwindcss/lib/util/isKeyframeRule.js"
                validateConfig_js: str = "node_modules/tailwindcss/lib/util/validateConfig.js"
                negateValue_js: str = "node_modules/tailwindcss/lib/util/negateValue.js"
                normalizeConfig_js: str = "node_modules/tailwindcss/lib/util/normalizeConfig.js"
                prefixSelector_js: str = "node_modules/tailwindcss/lib/util/prefixSelector.js"
                getAllConfigs_js: str = "node_modules/tailwindcss/lib/util/getAllConfigs.js"
                transformThemeValue_js: str = "node_modules/tailwindcss/lib/util/transformThemeValue.js"
                validateFormalSyntax_js: str = "node_modules/tailwindcss/lib/util/validateFormalSyntax.js"
                configurePlugins_js: str = "node_modules/tailwindcss/lib/util/configurePlugins.js"
            util = _node_modules_tailwindcss_lib_util()

            class _node_modules_tailwindcss_lib_value_parser:
                parse_js: str = "node_modules/tailwindcss/lib/value-parser/parse.js"
                walk_js: str = "node_modules/tailwindcss/lib/value-parser/walk.js"
                unit_js: str = "node_modules/tailwindcss/lib/value-parser/unit.js"
                index_d_js: str = "node_modules/tailwindcss/lib/value-parser/index.d.js"
                index_js: str = "node_modules/tailwindcss/lib/value-parser/index.js"
                stringify_js: str = "node_modules/tailwindcss/lib/value-parser/stringify.js"
            value_parser = _node_modules_tailwindcss_lib_value_parser()

            class _node_modules_tailwindcss_lib_cli:
                index_js: str = "node_modules/tailwindcss/lib/cli/index.js"
                help: str = "node_modules/tailwindcss/lib/cli/help/index.js"
                init: str = "node_modules/tailwindcss/lib/cli/init/index.js"

                class _node_modules_tailwindcss_lib_cli_build:
                    utils_js: str = "node_modules/tailwindcss/lib/cli/build/utils.js"
                    watching_js: str = "node_modules/tailwindcss/lib/cli/build/watching.js"
                    index_js: str = "node_modules/tailwindcss/lib/cli/build/index.js"
                    plugin_js: str = "node_modules/tailwindcss/lib/cli/build/plugin.js"
                    deps_js: str = "node_modules/tailwindcss/lib/cli/build/deps.js"
                build = _node_modules_tailwindcss_lib_cli_build()
            cli = _node_modules_tailwindcss_lib_cli()

            class _node_modules_tailwindcss_lib_lib:
                defaultExtractor_js: str = "node_modules/tailwindcss/lib/lib/defaultExtractor.js"
                regex_js: str = "node_modules/tailwindcss/lib/lib/regex.js"
                load_config_js: str = "node_modules/tailwindcss/lib/lib/load-config.js"
                substituteScreenAtRules_js: str = "node_modules/tailwindcss/lib/lib/substituteScreenAtRules.js"
                evaluateTailwindFunctions_js: str = "node_modules/tailwindcss/lib/lib/evaluateTailwindFunctions.js"
                expandTailwindAtRules_js: str = "node_modules/tailwindcss/lib/lib/expandTailwindAtRules.js"
                normalizeTailwindDirectives_js: str = "node_modules/tailwindcss/lib/lib/normalizeTailwindDirectives.js"
                setupTrackingContext_js: str = "node_modules/tailwindcss/lib/lib/setupTrackingContext.js"
                content_js: str = "node_modules/tailwindcss/lib/lib/content.js"
                sharedState_js: str = "node_modules/tailwindcss/lib/lib/sharedState.js"
                getModuleDependencies_js: str = "node_modules/tailwindcss/lib/lib/getModuleDependencies.js"
                findAtConfigPath_js: str = "node_modules/tailwindcss/lib/lib/findAtConfigPath.js"
                remap_bitfield_js: str = "node_modules/tailwindcss/lib/lib/remap-bitfield.js"
                offsets_js: str = "node_modules/tailwindcss/lib/lib/offsets.js"
                partitionApplyAtRules_js: str = "node_modules/tailwindcss/lib/lib/partitionApplyAtRules.js"
                setupContextUtils_js: str = "node_modules/tailwindcss/lib/lib/setupContextUtils.js"
                cacheInvalidation_js: str = "node_modules/tailwindcss/lib/lib/cacheInvalidation.js"
                collapseAdjacentRules_js: str = "node_modules/tailwindcss/lib/lib/collapseAdjacentRules.js"
                collapseDuplicateDeclarations_js: str = "node_modules/tailwindcss/lib/lib/collapseDuplicateDeclarations.js"
                resolveDefaultsAtRules_js: str = "node_modules/tailwindcss/lib/lib/resolveDefaultsAtRules.js"
                generateRules_js: str = "node_modules/tailwindcss/lib/lib/generateRules.js"
                expandApplyAtRules_js: str = "node_modules/tailwindcss/lib/lib/expandApplyAtRules.js"
            lib = _node_modules_tailwindcss_lib_lib()
            css: str = "node_modules/tailwindcss/lib/css/preflight.css"

            class _node_modules_tailwindcss_lib_postcss_plugins:

                class _node_modules_tailwindcss_lib_postcss_plugins_nesting:
                    index_js: str = "node_modules/tailwindcss/lib/postcss-plugins/nesting/index.js"
                    plugin_js: str = "node_modules/tailwindcss/lib/postcss-plugins/nesting/plugin.js"
                nesting = _node_modules_tailwindcss_lib_postcss_plugins_nesting()
            postcss_plugins = _node_modules_tailwindcss_lib_postcss_plugins()

            class _node_modules_tailwindcss_lib_public:
                create_plugin_js: str = "node_modules/tailwindcss/lib/public/create-plugin.js"
                load_config_js: str = "node_modules/tailwindcss/lib/public/load-config.js"
                colors_js: str = "node_modules/tailwindcss/lib/public/colors.js"
                resolve_config_js: str = "node_modules/tailwindcss/lib/public/resolve-config.js"
                default_theme_js: str = "node_modules/tailwindcss/lib/public/default-theme.js"
                default_config_js: str = "node_modules/tailwindcss/lib/public/default-config.js"
            public = _node_modules_tailwindcss_lib_public()
        lib = _node_modules_tailwindcss_lib()
        nesting: str = "node_modules/tailwindcss/nesting/index.js"

        class _node_modules_tailwindcss_scripts:
            release_channel_js: str = "node_modules/tailwindcss/scripts/release-channel.js"
            generate_types_js: str = "node_modules/tailwindcss/scripts/generate-types.js"
            create_plugin_list_js: str = "node_modules/tailwindcss/scripts/create-plugin-list.js"
            release_notes_js: str = "node_modules/tailwindcss/scripts/release-notes.js"
            type_utils_js: str = "node_modules/tailwindcss/scripts/type-utils.js"
        scripts = _node_modules_tailwindcss_scripts()

        class _node_modules_tailwindcss_stubs:
            config_full_js: str = "node_modules/tailwindcss/stubs/config.full.js"
            tailwind_config_js: str = "node_modules/tailwindcss/stubs/tailwind.config.js"
            config_simple_js: str = "node_modules/tailwindcss/stubs/config.simple.js"
            postcss_config_js: str = "node_modules/tailwindcss/stubs/postcss.config.js"
        stubs = _node_modules_tailwindcss_stubs()
    tailwindcss = _node_modules_tailwindcss()

    class _node_modules_entities:

        class _node_modules_entities_lib:
            index_js: str = "node_modules/entities/lib/index.js"
            decode_codepoint_js: str = "node_modules/entities/lib/decode_codepoint.js"
            decode_js: str = "node_modules/entities/lib/decode.js"
            encode_js: str = "node_modules/entities/lib/encode.js"
        lib = _node_modules_entities_lib()
    entities = _node_modules_entities()

    class _node_modules_picocolors:
        picocolors_js: str = "node_modules/picocolors/picocolors.js"
        picocolors_browser_js: str = "node_modules/picocolors/picocolors.browser.js"
    picocolors = _node_modules_picocolors()

    class _node_modules_generic_names:
        index_js: str = "node_modules/generic-names/index.js"
    generic_names = _node_modules_generic_names()

    class _node_modules_postcss_discard_empty:
        src: str = "node_modules/postcss-discard-empty/src/index.js"
    postcss_discard_empty = _node_modules_postcss_discard_empty()

    class _node_modules_stylehacks:

        class _node_modules_stylehacks_src:
            isMixin_js: str = "node_modules/stylehacks/src/isMixin.js"
            index_js: str = "node_modules/stylehacks/src/index.js"
            exists_js: str = "node_modules/stylehacks/src/exists.js"
            plugin_js: str = "node_modules/stylehacks/src/plugin.js"

            class _node_modules_stylehacks_src_plugins:
                trailingSlashComma_js: str = "node_modules/stylehacks/src/plugins/trailingSlashComma.js"
                mediaSlash0Slash9_js: str = "node_modules/stylehacks/src/plugins/mediaSlash0Slash9.js"
                leadingStar_js: str = "node_modules/stylehacks/src/plugins/leadingStar.js"
                index_js: str = "node_modules/stylehacks/src/plugins/index.js"
                htmlCombinatorCommentBody_js: str = "node_modules/stylehacks/src/plugins/htmlCombinatorCommentBody.js"
                leadingUnderscore_js: str = "node_modules/stylehacks/src/plugins/leadingUnderscore.js"
                important_js: str = "node_modules/stylehacks/src/plugins/important.js"
                mediaSlash0_js: str = "node_modules/stylehacks/src/plugins/mediaSlash0.js"
                starHtml_js: str = "node_modules/stylehacks/src/plugins/starHtml.js"
                mediaSlash9_js: str = "node_modules/stylehacks/src/plugins/mediaSlash9.js"
                slash9_js: str = "node_modules/stylehacks/src/plugins/slash9.js"
                bodyEmpty_js: str = "node_modules/stylehacks/src/plugins/bodyEmpty.js"
                htmlFirstChild_js: str = "node_modules/stylehacks/src/plugins/htmlFirstChild.js"
            plugins = _node_modules_stylehacks_src_plugins()

            class _node_modules_stylehacks_src_dictionary:
                postcss_js: str = "node_modules/stylehacks/src/dictionary/postcss.js"
                browsers_js: str = "node_modules/stylehacks/src/dictionary/browsers.js"
                identifiers_js: str = "node_modules/stylehacks/src/dictionary/identifiers.js"
                tags_js: str = "node_modules/stylehacks/src/dictionary/tags.js"
            dictionary = _node_modules_stylehacks_src_dictionary()
        src = _node_modules_stylehacks_src()
    stylehacks = _node_modules_stylehacks()

    class _node_modules_browserslist:
        parse_js: str = "node_modules/browserslist/parse.js"
        cli_js: str = "node_modules/browserslist/cli.js"
        index_js: str = "node_modules/browserslist/index.js"
        node_js: str = "node_modules/browserslist/node.js"
        browser_js: str = "node_modules/browserslist/browser.js"
        error_js: str = "node_modules/browserslist/error.js"
    browserslist = _node_modules_browserslist()

    class _node_modules_reusify:
        test_js: str = "node_modules/reusify/test.js"
        reusify_js: str = "node_modules/reusify/reusify.js"

        class _node_modules_reusify_benchmarks:
            fib_js: str = "node_modules/reusify/benchmarks/fib.js"
            reuseNoCodeFunction_js: str = "node_modules/reusify/benchmarks/reuseNoCodeFunction.js"
            createNoCodeFunction_js: str = "node_modules/reusify/benchmarks/createNoCodeFunction.js"
        benchmarks = _node_modules_reusify_benchmarks()
    reusify = _node_modules_reusify()

    class _node_modules_postcss_normalize_string:
        src: str = "node_modules/postcss-normalize-string/src/index.js"
    postcss_normalize_string = _node_modules_postcss_normalize_string()

    class _node_modules_wrap_ansi:
        index_js: str = "node_modules/wrap-ansi/index.js"

        class _node_modules_wrap_ansi_node_modules:
            ansi_styles: str = "node_modules/wrap-ansi/node_modules/ansi-styles/index.js"
        node_modules = _node_modules_wrap_ansi_node_modules()
    wrap_ansi = _node_modules_wrap_ansi()
    string_width: str = "node_modules/string-width/index.js"

    class _node_modules_pkgjs:

        class _node_modules_pkgjs_parseargs:
            utils_js: str = "node_modules/@pkgjs/parseargs/utils.js"
            index_js: str = "node_modules/@pkgjs/parseargs/index.js"

            class _node_modules_pkgjs_parseargs_examples:
                negate_js: str = "node_modules/@pkgjs/parseargs/examples/negate.js"
                simple_hard_coded_js: str = "node_modules/@pkgjs/parseargs/examples/simple-hard-coded.js"
                limit_long_syntax_js: str = "node_modules/@pkgjs/parseargs/examples/limit-long-syntax.js"
                no_repeated_options_js: str = "node_modules/@pkgjs/parseargs/examples/no-repeated-options.js"
                is_default_value_js: str = "node_modules/@pkgjs/parseargs/examples/is-default-value.js"
            examples = _node_modules_pkgjs_parseargs_examples()

            class _node_modules_pkgjs_parseargs_internal:
                errors_js: str = "node_modules/@pkgjs/parseargs/internal/errors.js"
                util_js: str = "node_modules/@pkgjs/parseargs/internal/util.js"
                primordials_js: str = "node_modules/@pkgjs/parseargs/internal/primordials.js"
                validators_js: str = "node_modules/@pkgjs/parseargs/internal/validators.js"
            internal = _node_modules_pkgjs_parseargs_internal()
        parseargs = _node_modules_pkgjs_parseargs()
    pkgjs = _node_modules_pkgjs()
    lodash_uniq: str = "node_modules/lodash.uniq/index.js"
    is_number: str = "node_modules/is-number/index.js"

    class _node_modules_commander:
        index_js: str = "node_modules/commander/index.js"
    commander = _node_modules_commander()

    class _node_modules_caniuse_lite:

        class _node_modules_caniuse_lite_dist:

            class _node_modules_caniuse_lite_dist_unpacker:
                browserVersions_js: str = "node_modules/caniuse-lite/dist/unpacker/browserVersions.js"
                browsers_js: str = "node_modules/caniuse-lite/dist/unpacker/browsers.js"
                features_js: str = "node_modules/caniuse-lite/dist/unpacker/features.js"
                index_js: str = "node_modules/caniuse-lite/dist/unpacker/index.js"
                agents_js: str = "node_modules/caniuse-lite/dist/unpacker/agents.js"
                feature_js: str = "node_modules/caniuse-lite/dist/unpacker/feature.js"
                region_js: str = "node_modules/caniuse-lite/dist/unpacker/region.js"
            unpacker = _node_modules_caniuse_lite_dist_unpacker()

            class _node_modules_caniuse_lite_dist_lib:
                supported_js: str = "node_modules/caniuse-lite/dist/lib/supported.js"
                statuses_js: str = "node_modules/caniuse-lite/dist/lib/statuses.js"
            lib = _node_modules_caniuse_lite_dist_lib()
        dist = _node_modules_caniuse_lite_dist()

        class _node_modules_caniuse_lite_data:
            browserVersions_js: str = "node_modules/caniuse-lite/data/browserVersions.js"
            browsers_js: str = "node_modules/caniuse-lite/data/browsers.js"
            features_js: str = "node_modules/caniuse-lite/data/features.js"
            agents_js: str = "node_modules/caniuse-lite/data/agents.js"

            class _node_modules_caniuse_lite_data_regions:
                CM_js: str = "node_modules/caniuse-lite/data/regions/CM.js"
                TZ_js: str = "node_modules/caniuse-lite/data/regions/TZ.js"
                alt_an_js: str = "node_modules/caniuse-lite/data/regions/alt-an.js"
                TG_js: str = "node_modules/caniuse-lite/data/regions/TG.js"
                HK_js: str = "node_modules/caniuse-lite/data/regions/HK.js"
                GB_js: str = "node_modules/caniuse-lite/data/regions/GB.js"
                SR_js: str = "node_modules/caniuse-lite/data/regions/SR.js"
                ZW_js: str = "node_modules/caniuse-lite/data/regions/ZW.js"
                AL_js: str = "node_modules/caniuse-lite/data/regions/AL.js"
                PA_js: str = "node_modules/caniuse-lite/data/regions/PA.js"
                BF_js: str = "node_modules/caniuse-lite/data/regions/BF.js"
                YE_js: str = "node_modules/caniuse-lite/data/regions/YE.js"
                MY_js: str = "node_modules/caniuse-lite/data/regions/MY.js"
                TW_js: str = "node_modules/caniuse-lite/data/regions/TW.js"
                PM_js: str = "node_modules/caniuse-lite/data/regions/PM.js"
                NE_js: str = "node_modules/caniuse-lite/data/regions/NE.js"
                CV_js: str = "node_modules/caniuse-lite/data/regions/CV.js"
                MH_js: str = "node_modules/caniuse-lite/data/regions/MH.js"
                MP_js: str = "node_modules/caniuse-lite/data/regions/MP.js"
                GF_js: str = "node_modules/caniuse-lite/data/regions/GF.js"
                ML_js: str = "node_modules/caniuse-lite/data/regions/ML.js"
                alt_as_js: str = "node_modules/caniuse-lite/data/regions/alt-as.js"
                RO_js: str = "node_modules/caniuse-lite/data/regions/RO.js"
                DM_js: str = "node_modules/caniuse-lite/data/regions/DM.js"
                TR_js: str = "node_modules/caniuse-lite/data/regions/TR.js"
                GG_js: str = "node_modules/caniuse-lite/data/regions/GG.js"
                SH_js: str = "node_modules/caniuse-lite/data/regions/SH.js"
                HT_js: str = "node_modules/caniuse-lite/data/regions/HT.js"
                alt_na_js: str = "node_modules/caniuse-lite/data/regions/alt-na.js"
                NU_js: str = "node_modules/caniuse-lite/data/regions/NU.js"
                QA_js: str = "node_modules/caniuse-lite/data/regions/QA.js"
                TV_js: str = "node_modules/caniuse-lite/data/regions/TV.js"
                LR_js: str = "node_modules/caniuse-lite/data/regions/LR.js"
                VE_js: str = "node_modules/caniuse-lite/data/regions/VE.js"
                LT_js: str = "node_modules/caniuse-lite/data/regions/LT.js"
                WF_js: str = "node_modules/caniuse-lite/data/regions/WF.js"
                ES_js: str = "node_modules/caniuse-lite/data/regions/ES.js"
                EG_js: str = "node_modules/caniuse-lite/data/regions/EG.js"
                BT_js: str = "node_modules/caniuse-lite/data/regions/BT.js"
                IR_js: str = "node_modules/caniuse-lite/data/regions/IR.js"
                AM_js: str = "node_modules/caniuse-lite/data/regions/AM.js"
                SM_js: str = "node_modules/caniuse-lite/data/regions/SM.js"
                GW_js: str = "node_modules/caniuse-lite/data/regions/GW.js"
                SZ_js: str = "node_modules/caniuse-lite/data/regions/SZ.js"
                IE_js: str = "node_modules/caniuse-lite/data/regions/IE.js"
                LB_js: str = "node_modules/caniuse-lite/data/regions/LB.js"
                AW_js: str = "node_modules/caniuse-lite/data/regions/AW.js"
                MO_js: str = "node_modules/caniuse-lite/data/regions/MO.js"
                alt_oc_js: str = "node_modules/caniuse-lite/data/regions/alt-oc.js"
                BH_js: str = "node_modules/caniuse-lite/data/regions/BH.js"
                GH_js: str = "node_modules/caniuse-lite/data/regions/GH.js"
                MU_js: str = "node_modules/caniuse-lite/data/regions/MU.js"
                PL_js: str = "node_modules/caniuse-lite/data/regions/PL.js"
                KE_js: str = "node_modules/caniuse-lite/data/regions/KE.js"
                ID_js: str = "node_modules/caniuse-lite/data/regions/ID.js"
                GN_js: str = "node_modules/caniuse-lite/data/regions/GN.js"
                MT_js: str = "node_modules/caniuse-lite/data/regions/MT.js"
                NR_js: str = "node_modules/caniuse-lite/data/regions/NR.js"
                MN_js: str = "node_modules/caniuse-lite/data/regions/MN.js"
                BW_js: str = "node_modules/caniuse-lite/data/regions/BW.js"
                AR_js: str = "node_modules/caniuse-lite/data/regions/AR.js"
                UY_js: str = "node_modules/caniuse-lite/data/regions/UY.js"
                TJ_js: str = "node_modules/caniuse-lite/data/regions/TJ.js"
                KH_js: str = "node_modules/caniuse-lite/data/regions/KH.js"
                AX_js: str = "node_modules/caniuse-lite/data/regions/AX.js"
                BI_js: str = "node_modules/caniuse-lite/data/regions/BI.js"
                TL_js: str = "node_modules/caniuse-lite/data/regions/TL.js"
                TO_js: str = "node_modules/caniuse-lite/data/regions/TO.js"
                FI_js: str = "node_modules/caniuse-lite/data/regions/FI.js"
                TD_js: str = "node_modules/caniuse-lite/data/regions/TD.js"
                GL_js: str = "node_modules/caniuse-lite/data/regions/GL.js"
                TC_js: str = "node_modules/caniuse-lite/data/regions/TC.js"
                MC_js: str = "node_modules/caniuse-lite/data/regions/MC.js"
                alt_sa_js: str = "node_modules/caniuse-lite/data/regions/alt-sa.js"
                TM_js: str = "node_modules/caniuse-lite/data/regions/TM.js"
                SK_js: str = "node_modules/caniuse-lite/data/regions/SK.js"
                TK_js: str = "node_modules/caniuse-lite/data/regions/TK.js"
                VI_js: str = "node_modules/caniuse-lite/data/regions/VI.js"
                NG_js: str = "node_modules/caniuse-lite/data/regions/NG.js"
                GU_js: str = "node_modules/caniuse-lite/data/regions/GU.js"
                SB_js: str = "node_modules/caniuse-lite/data/regions/SB.js"
                BE_js: str = "node_modules/caniuse-lite/data/regions/BE.js"
                LS_js: str = "node_modules/caniuse-lite/data/regions/LS.js"
                SI_js: str = "node_modules/caniuse-lite/data/regions/SI.js"
                LU_js: str = "node_modules/caniuse-lite/data/regions/LU.js"
                AF_js: str = "node_modules/caniuse-lite/data/regions/AF.js"
                HR_js: str = "node_modules/caniuse-lite/data/regions/HR.js"
                MA_js: str = "node_modules/caniuse-lite/data/regions/MA.js"
                VU_js: str = "node_modules/caniuse-lite/data/regions/VU.js"
                ZM_js: str = "node_modules/caniuse-lite/data/regions/ZM.js"
                CN_js: str = "node_modules/caniuse-lite/data/regions/CN.js"
                AG_js: str = "node_modules/caniuse-lite/data/regions/AG.js"
                UZ_js: str = "node_modules/caniuse-lite/data/regions/UZ.js"
                IM_js: str = "node_modules/caniuse-lite/data/regions/IM.js"
                BO_js: str = "node_modules/caniuse-lite/data/regions/BO.js"
                CZ_js: str = "node_modules/caniuse-lite/data/regions/CZ.js"
                SN_js: str = "node_modules/caniuse-lite/data/regions/SN.js"
                AS_js: str = "node_modules/caniuse-lite/data/regions/AS.js"
                FM_js: str = "node_modules/caniuse-lite/data/regions/FM.js"
                CI_js: str = "node_modules/caniuse-lite/data/regions/CI.js"
                KN_js: str = "node_modules/caniuse-lite/data/regions/KN.js"
                DJ_js: str = "node_modules/caniuse-lite/data/regions/DJ.js"
                MX_js: str = "node_modules/caniuse-lite/data/regions/MX.js"
                NF_js: str = "node_modules/caniuse-lite/data/regions/NF.js"
                PR_js: str = "node_modules/caniuse-lite/data/regions/PR.js"
                AU_js: str = "node_modules/caniuse-lite/data/regions/AU.js"
                FK_js: str = "node_modules/caniuse-lite/data/regions/FK.js"
                alt_af_js: str = "node_modules/caniuse-lite/data/regions/alt-af.js"
                KW_js: str = "node_modules/caniuse-lite/data/regions/KW.js"
                SV_js: str = "node_modules/caniuse-lite/data/regions/SV.js"
                KP_js: str = "node_modules/caniuse-lite/data/regions/KP.js"
                IQ_js: str = "node_modules/caniuse-lite/data/regions/IQ.js"
                HN_js: str = "node_modules/caniuse-lite/data/regions/HN.js"
                IS_js: str = "node_modules/caniuse-lite/data/regions/IS.js"
                AT_js: str = "node_modules/caniuse-lite/data/regions/AT.js"
                BY_js: str = "node_modules/caniuse-lite/data/regions/BY.js"
                ER_js: str = "node_modules/caniuse-lite/data/regions/ER.js"
                TT_js: str = "node_modules/caniuse-lite/data/regions/TT.js"
                BZ_js: str = "node_modules/caniuse-lite/data/regions/BZ.js"
                MR_js: str = "node_modules/caniuse-lite/data/regions/MR.js"
                CY_js: str = "node_modules/caniuse-lite/data/regions/CY.js"
                SG_js: str = "node_modules/caniuse-lite/data/regions/SG.js"
                PW_js: str = "node_modules/caniuse-lite/data/regions/PW.js"
                PF_js: str = "node_modules/caniuse-lite/data/regions/PF.js"
                CU_js: str = "node_modules/caniuse-lite/data/regions/CU.js"
                GD_js: str = "node_modules/caniuse-lite/data/regions/GD.js"
                TN_js: str = "node_modules/caniuse-lite/data/regions/TN.js"
                GA_js: str = "node_modules/caniuse-lite/data/regions/GA.js"
                NO_js: str = "node_modules/caniuse-lite/data/regions/NO.js"
                SY_js: str = "node_modules/caniuse-lite/data/regions/SY.js"
                GY_js: str = "node_modules/caniuse-lite/data/regions/GY.js"
                AE_js: str = "node_modules/caniuse-lite/data/regions/AE.js"
                IT_js: str = "node_modules/caniuse-lite/data/regions/IT.js"
                AI_js: str = "node_modules/caniuse-lite/data/regions/AI.js"
                KY_js: str = "node_modules/caniuse-lite/data/regions/KY.js"
                RW_js: str = "node_modules/caniuse-lite/data/regions/RW.js"
                BM_js: str = "node_modules/caniuse-lite/data/regions/BM.js"
                ST_js: str = "node_modules/caniuse-lite/data/regions/ST.js"
                BG_js: str = "node_modules/caniuse-lite/data/regions/BG.js"
                VN_js: str = "node_modules/caniuse-lite/data/regions/VN.js"
                RS_js: str = "node_modules/caniuse-lite/data/regions/RS.js"
                MQ_js: str = "node_modules/caniuse-lite/data/regions/MQ.js"
                OM_js: str = "node_modules/caniuse-lite/data/regions/OM.js"
                VC_js: str = "node_modules/caniuse-lite/data/regions/VC.js"
                GI_js: str = "node_modules/caniuse-lite/data/regions/GI.js"
                BN_js: str = "node_modules/caniuse-lite/data/regions/BN.js"
                alt_eu_js: str = "node_modules/caniuse-lite/data/regions/alt-eu.js"
                NL_js: str = "node_modules/caniuse-lite/data/regions/NL.js"
                VA_js: str = "node_modules/caniuse-lite/data/regions/VA.js"
                NI_js: str = "node_modules/caniuse-lite/data/regions/NI.js"
                MZ_js: str = "node_modules/caniuse-lite/data/regions/MZ.js"
                PE_js: str = "node_modules/caniuse-lite/data/regions/PE.js"
                TH_js: str = "node_modules/caniuse-lite/data/regions/TH.js"
                YT_js: str = "node_modules/caniuse-lite/data/regions/YT.js"
                AD_js: str = "node_modules/caniuse-lite/data/regions/AD.js"
                SE_js: str = "node_modules/caniuse-lite/data/regions/SE.js"
                KG_js: str = "node_modules/caniuse-lite/data/regions/KG.js"
                PS_js: str = "node_modules/caniuse-lite/data/regions/PS.js"
                VG_js: str = "node_modules/caniuse-lite/data/regions/VG.js"
                DZ_js: str = "node_modules/caniuse-lite/data/regions/DZ.js"
                DK_js: str = "node_modules/caniuse-lite/data/regions/DK.js"
                CD_js: str = "node_modules/caniuse-lite/data/regions/CD.js"
                AO_js: str = "node_modules/caniuse-lite/data/regions/AO.js"
                NA_js: str = "node_modules/caniuse-lite/data/regions/NA.js"
                LV_js: str = "node_modules/caniuse-lite/data/regions/LV.js"
                LI_js: str = "node_modules/caniuse-lite/data/regions/LI.js"
                IN_js: str = "node_modules/caniuse-lite/data/regions/IN.js"
                CO_js: str = "node_modules/caniuse-lite/data/regions/CO.js"
                CK_js: str = "node_modules/caniuse-lite/data/regions/CK.js"
                BA_js: str = "node_modules/caniuse-lite/data/regions/BA.js"
                ZA_js: str = "node_modules/caniuse-lite/data/regions/ZA.js"
                RE_js: str = "node_modules/caniuse-lite/data/regions/RE.js"
                DO_js: str = "node_modules/caniuse-lite/data/regions/DO.js"
                GE_js: str = "node_modules/caniuse-lite/data/regions/GE.js"
                CF_js: str = "node_modules/caniuse-lite/data/regions/CF.js"
                WS_js: str = "node_modules/caniuse-lite/data/regions/WS.js"
                UA_js: str = "node_modules/caniuse-lite/data/regions/UA.js"
                SC_js: str = "node_modules/caniuse-lite/data/regions/SC.js"
                AZ_js: str = "node_modules/caniuse-lite/data/regions/AZ.js"
                GQ_js: str = "node_modules/caniuse-lite/data/regions/GQ.js"
                DE_js: str = "node_modules/caniuse-lite/data/regions/DE.js"
                LY_js: str = "node_modules/caniuse-lite/data/regions/LY.js"
                JO_js: str = "node_modules/caniuse-lite/data/regions/JO.js"
                KR_js: str = "node_modules/caniuse-lite/data/regions/KR.js"
                IL_js: str = "node_modules/caniuse-lite/data/regions/IL.js"
                FR_js: str = "node_modules/caniuse-lite/data/regions/FR.js"
                BB_js: str = "node_modules/caniuse-lite/data/regions/BB.js"
                LA_js: str = "node_modules/caniuse-lite/data/regions/LA.js"
                PH_js: str = "node_modules/caniuse-lite/data/regions/PH.js"
                LK_js: str = "node_modules/caniuse-lite/data/regions/LK.js"
                BR_js: str = "node_modules/caniuse-lite/data/regions/BR.js"
                PG_js: str = "node_modules/caniuse-lite/data/regions/PG.js"
                NZ_js: str = "node_modules/caniuse-lite/data/regions/NZ.js"
                BD_js: str = "node_modules/caniuse-lite/data/regions/BD.js"
                NP_js: str = "node_modules/caniuse-lite/data/regions/NP.js"
                PK_js: str = "node_modules/caniuse-lite/data/regions/PK.js"
                PY_js: str = "node_modules/caniuse-lite/data/regions/PY.js"
                CA_js: str = "node_modules/caniuse-lite/data/regions/CA.js"
                SL_js: str = "node_modules/caniuse-lite/data/regions/SL.js"
                LC_js: str = "node_modules/caniuse-lite/data/regions/LC.js"
                CH_js: str = "node_modules/caniuse-lite/data/regions/CH.js"
                NC_js: str = "node_modules/caniuse-lite/data/regions/NC.js"
                JM_js: str = "node_modules/caniuse-lite/data/regions/JM.js"
                JP_js: str = "node_modules/caniuse-lite/data/regions/JP.js"
                CL_js: str = "node_modules/caniuse-lite/data/regions/CL.js"
                MK_js: str = "node_modules/caniuse-lite/data/regions/MK.js"
                KI_js: str = "node_modules/caniuse-lite/data/regions/KI.js"
                BJ_js: str = "node_modules/caniuse-lite/data/regions/BJ.js"
                KM_js: str = "node_modules/caniuse-lite/data/regions/KM.js"
                MD_js: str = "node_modules/caniuse-lite/data/regions/MD.js"
                KZ_js: str = "node_modules/caniuse-lite/data/regions/KZ.js"
                MG_js: str = "node_modules/caniuse-lite/data/regions/MG.js"
                MW_js: str = "node_modules/caniuse-lite/data/regions/MW.js"
                BS_js: str = "node_modules/caniuse-lite/data/regions/BS.js"
                JE_js: str = "node_modules/caniuse-lite/data/regions/JE.js"
                GT_js: str = "node_modules/caniuse-lite/data/regions/GT.js"
                FJ_js: str = "node_modules/caniuse-lite/data/regions/FJ.js"
                CR_js: str = "node_modules/caniuse-lite/data/regions/CR.js"
                SO_js: str = "node_modules/caniuse-lite/data/regions/SO.js"
                CX_js: str = "node_modules/caniuse-lite/data/regions/CX.js"
                MV_js: str = "node_modules/caniuse-lite/data/regions/MV.js"
                SD_js: str = "node_modules/caniuse-lite/data/regions/SD.js"
                EC_js: str = "node_modules/caniuse-lite/data/regions/EC.js"
                EE_js: str = "node_modules/caniuse-lite/data/regions/EE.js"
                MS_js: str = "node_modules/caniuse-lite/data/regions/MS.js"
                ET_js: str = "node_modules/caniuse-lite/data/regions/ET.js"
                GP_js: str = "node_modules/caniuse-lite/data/regions/GP.js"
                HU_js: str = "node_modules/caniuse-lite/data/regions/HU.js"
                US_js: str = "node_modules/caniuse-lite/data/regions/US.js"
                RU_js: str = "node_modules/caniuse-lite/data/regions/RU.js"
                GR_js: str = "node_modules/caniuse-lite/data/regions/GR.js"
                FO_js: str = "node_modules/caniuse-lite/data/regions/FO.js"
                PN_js: str = "node_modules/caniuse-lite/data/regions/PN.js"
                alt_ww_js: str = "node_modules/caniuse-lite/data/regions/alt-ww.js"
                MM_js: str = "node_modules/caniuse-lite/data/regions/MM.js"
                PT_js: str = "node_modules/caniuse-lite/data/regions/PT.js"
                UG_js: str = "node_modules/caniuse-lite/data/regions/UG.js"
                GM_js: str = "node_modules/caniuse-lite/data/regions/GM.js"
                SA_js: str = "node_modules/caniuse-lite/data/regions/SA.js"
                ME_js: str = "node_modules/caniuse-lite/data/regions/ME.js"
                CG_js: str = "node_modules/caniuse-lite/data/regions/CG.js"
            regions = _node_modules_caniuse_lite_data_regions()

            class _node_modules_caniuse_lite_data_features:
                mdn_text_decoration_line_js: str = "node_modules/caniuse-lite/data/features/mdn-text-decoration-line.js"
                childnode_remove_js: str = "node_modules/caniuse-lite/data/features/childnode-remove.js"
                font_variant_alternates_js: str = "node_modules/caniuse-lite/data/features/font-variant-alternates.js"
                webvtt_js: str = "node_modules/caniuse-lite/data/features/webvtt.js"
                pad_start_end_js: str = "node_modules/caniuse-lite/data/features/pad-start-end.js"
                link_rel_prefetch_js: str = "node_modules/caniuse-lite/data/features/link-rel-prefetch.js"
                css_sel3_js: str = "node_modules/caniuse-lite/data/features/css-sel3.js"
                woff2_js: str = "node_modules/caniuse-lite/data/features/woff2.js"
                css_display_contents_js: str = "node_modules/caniuse-lite/data/features/css-display-contents.js"
                xhr2_js: str = "node_modules/caniuse-lite/data/features/xhr2.js"
                multibackgrounds_js: str = "node_modules/caniuse-lite/data/features/multibackgrounds.js"
                ime_js: str = "node_modules/caniuse-lite/data/features/ime.js"
                jpegxr_js: str = "node_modules/caniuse-lite/data/features/jpegxr.js"
                js_regexp_lookbehind_js: str = "node_modules/caniuse-lite/data/features/js-regexp-lookbehind.js"
                wasm_extended_const_js: str = "node_modules/caniuse-lite/data/features/wasm-extended-const.js"
                css_read_only_write_js: str = "node_modules/caniuse-lite/data/features/css-read-only-write.js"
                readonly_attr_js: str = "node_modules/caniuse-lite/data/features/readonly-attr.js"
                mathml_js: str = "node_modules/caniuse-lite/data/features/mathml.js"
                inline_block_js: str = "node_modules/caniuse-lite/data/features/inline-block.js"
                rellist_js: str = "node_modules/caniuse-lite/data/features/rellist.js"
                use_strict_js: str = "node_modules/caniuse-lite/data/features/use-strict.js"
                bigint_js: str = "node_modules/caniuse-lite/data/features/bigint.js"
                web_animation_js: str = "node_modules/caniuse-lite/data/features/web-animation.js"
                notifications_js: str = "node_modules/caniuse-lite/data/features/notifications.js"
                png_alpha_js: str = "node_modules/caniuse-lite/data/features/png-alpha.js"
                form_validation_js: str = "node_modules/caniuse-lite/data/features/form-validation.js"
                css_env_function_js: str = "node_modules/caniuse-lite/data/features/css-env-function.js"
                css_appearance_js: str = "node_modules/caniuse-lite/data/features/css-appearance.js"
                keyboardevent_code_js: str = "node_modules/caniuse-lite/data/features/keyboardevent-code.js"
                dialog_js: str = "node_modules/caniuse-lite/data/features/dialog.js"
                webgpu_js: str = "node_modules/caniuse-lite/data/features/webgpu.js"
                input_range_js: str = "node_modules/caniuse-lite/data/features/input-range.js"
                hashchange_js: str = "node_modules/caniuse-lite/data/features/hashchange.js"
                css_repeating_gradients_js: str = "node_modules/caniuse-lite/data/features/css-repeating-gradients.js"
                dom_range_js: str = "node_modules/caniuse-lite/data/features/dom-range.js"
                history_js: str = "node_modules/caniuse-lite/data/features/history.js"
                css_clip_path_js: str = "node_modules/caniuse-lite/data/features/css-clip-path.js"
                proxy_js: str = "node_modules/caniuse-lite/data/features/proxy.js"
                testfeat_js: str = "node_modules/caniuse-lite/data/features/testfeat.js"
                css3_cursors_newer_js: str = "node_modules/caniuse-lite/data/features/css3-cursors-newer.js"
                word_break_js: str = "node_modules/caniuse-lite/data/features/word-break.js"
                cookie_store_api_js: str = "node_modules/caniuse-lite/data/features/cookie-store-api.js"
                flac_js: str = "node_modules/caniuse-lite/data/features/flac.js"
                input_autocomplete_onoff_js: str = "node_modules/caniuse-lite/data/features/input-autocomplete-onoff.js"
                css_text_indent_js: str = "node_modules/caniuse-lite/data/features/css-text-indent.js"
                payment_request_js: str = "node_modules/caniuse-lite/data/features/payment-request.js"
                broadcastchannel_js: str = "node_modules/caniuse-lite/data/features/broadcastchannel.js"
                mdn_css_backdrop_pseudo_element_js: str = "node_modules/caniuse-lite/data/features/mdn-css-backdrop-pseudo-element.js"
                font_family_system_ui_js: str = "node_modules/caniuse-lite/data/features/font-family-system-ui.js"
                passive_event_listener_js: str = "node_modules/caniuse-lite/data/features/passive-event-listener.js"
                array_find_js: str = "node_modules/caniuse-lite/data/features/array-find.js"
                svg_filters_js: str = "node_modules/caniuse-lite/data/features/svg-filters.js"
                css_math_functions_js: str = "node_modules/caniuse-lite/data/features/css-math-functions.js"
                iframe_srcdoc_js: str = "node_modules/caniuse-lite/data/features/iframe-srcdoc.js"
                magnetometer_js: str = "node_modules/caniuse-lite/data/features/magnetometer.js"
                es6_number_js: str = "node_modules/caniuse-lite/data/features/es6-number.js"
                css_font_stretch_js: str = "node_modules/caniuse-lite/data/features/css-font-stretch.js"
                focusin_focusout_events_js: str = "node_modules/caniuse-lite/data/features/focusin-focusout-events.js"
                background_repeat_round_space_js: str = "node_modules/caniuse-lite/data/features/background-repeat-round-space.js"
                css_paged_media_js: str = "node_modules/caniuse-lite/data/features/css-paged-media.js"
                ogv_js: str = "node_modules/caniuse-lite/data/features/ogv.js"
                css_overscroll_behavior_js: str = "node_modules/caniuse-lite/data/features/css-overscroll-behavior.js"
                battery_status_js: str = "node_modules/caniuse-lite/data/features/battery-status.js"
                template_js: str = "node_modules/caniuse-lite/data/features/template.js"
                registerprotocolhandler_js: str = "node_modules/caniuse-lite/data/features/registerprotocolhandler.js"
                date_tolocaledatestring_js: str = "node_modules/caniuse-lite/data/features/date-tolocaledatestring.js"
                iframe_seamless_js: str = "node_modules/caniuse-lite/data/features/iframe-seamless.js"
                intrinsic_width_js: str = "node_modules/caniuse-lite/data/features/intrinsic-width.js"
                viewport_unit_variants_js: str = "node_modules/caniuse-lite/data/features/viewport-unit-variants.js"
                online_status_js: str = "node_modules/caniuse-lite/data/features/online-status.js"
                prefers_color_scheme_js: str = "node_modules/caniuse-lite/data/features/prefers-color-scheme.js"
                shadowdomv1_js: str = "node_modules/caniuse-lite/data/features/shadowdomv1.js"
                css_all_js: str = "node_modules/caniuse-lite/data/features/css-all.js"
                accelerometer_js: str = "node_modules/caniuse-lite/data/features/accelerometer.js"
                video_js: str = "node_modules/caniuse-lite/data/features/video.js"
                es6_js: str = "node_modules/caniuse-lite/data/features/es6.js"
                css_letter_spacing_js: str = "node_modules/caniuse-lite/data/features/css-letter-spacing.js"
                http3_js: str = "node_modules/caniuse-lite/data/features/http3.js"
                css_default_pseudo_js: str = "node_modules/caniuse-lite/data/features/css-default-pseudo.js"
                input_datetime_js: str = "node_modules/caniuse-lite/data/features/input-datetime.js"
                lazyload_js: str = "node_modules/caniuse-lite/data/features/lazyload.js"
                css3_colors_js: str = "node_modules/caniuse-lite/data/features/css3-colors.js"
                atob_btoa_js: str = "node_modules/caniuse-lite/data/features/atob-btoa.js"
                beacon_js: str = "node_modules/caniuse-lite/data/features/beacon.js"
                mpeg_dash_js: str = "node_modules/caniuse-lite/data/features/mpeg-dash.js"
                script_async_js: str = "node_modules/caniuse-lite/data/features/script-async.js"
                link_rel_prerender_js: str = "node_modules/caniuse-lite/data/features/link-rel-prerender.js"
                css_filter_function_js: str = "node_modules/caniuse-lite/data/features/css-filter-function.js"
                input_placeholder_js: str = "node_modules/caniuse-lite/data/features/input-placeholder.js"
                subresource_bundling_js: str = "node_modules/caniuse-lite/data/features/subresource-bundling.js"
                kerning_pairs_ligatures_js: str = "node_modules/caniuse-lite/data/features/kerning-pairs-ligatures.js"
                canvas_js: str = "node_modules/caniuse-lite/data/features/canvas.js"
                details_js: str = "node_modules/caniuse-lite/data/features/details.js"
                rel_noreferrer_js: str = "node_modules/caniuse-lite/data/features/rel-noreferrer.js"
                css_relative_colors_js: str = "node_modules/caniuse-lite/data/features/css-relative-colors.js"
                auxclick_js: str = "node_modules/caniuse-lite/data/features/auxclick.js"
                es6_module_dynamic_import_js: str = "node_modules/caniuse-lite/data/features/es6-module-dynamic-import.js"
                webkit_user_drag_js: str = "node_modules/caniuse-lite/data/features/webkit-user-drag.js"
                text_emphasis_js: str = "node_modules/caniuse-lite/data/features/text-emphasis.js"
                css_nth_child_of_js: str = "node_modules/caniuse-lite/data/features/css-nth-child-of.js"
                push_api_js: str = "node_modules/caniuse-lite/data/features/push-api.js"
                variable_fonts_js: str = "node_modules/caniuse-lite/data/features/variable-fonts.js"
                promises_js: str = "node_modules/caniuse-lite/data/features/promises.js"
                font_size_adjust_js: str = "node_modules/caniuse-lite/data/features/font-size-adjust.js"
                vibration_js: str = "node_modules/caniuse-lite/data/features/vibration.js"
                picture_in_picture_js: str = "node_modules/caniuse-lite/data/features/picture-in-picture.js"
                input_search_js: str = "node_modules/caniuse-lite/data/features/input-search.js"
                element_from_point_js: str = "node_modules/caniuse-lite/data/features/element-from-point.js"
                font_kerning_js: str = "node_modules/caniuse-lite/data/features/font-kerning.js"
                wasm_bulk_memory_js: str = "node_modules/caniuse-lite/data/features/wasm-bulk-memory.js"
                css_media_range_syntax_js: str = "node_modules/caniuse-lite/data/features/css-media-range-syntax.js"
                deviceorientation_js: str = "node_modules/caniuse-lite/data/features/deviceorientation.js"
                opus_js: str = "node_modules/caniuse-lite/data/features/opus.js"
                contenteditable_js: str = "node_modules/caniuse-lite/data/features/contenteditable.js"
                selectlist_js: str = "node_modules/caniuse-lite/data/features/selectlist.js"
                es6_generators_js: str = "node_modules/caniuse-lite/data/features/es6-generators.js"
                css_zoom_js: str = "node_modules/caniuse-lite/data/features/css-zoom.js"
                getrandomvalues_js: str = "node_modules/caniuse-lite/data/features/getrandomvalues.js"
                ol_reversed_js: str = "node_modules/caniuse-lite/data/features/ol-reversed.js"
                svg_html5_js: str = "node_modules/caniuse-lite/data/features/svg-html5.js"
                css_focus_visible_js: str = "node_modules/caniuse-lite/data/features/css-focus-visible.js"
                webp_js: str = "node_modules/caniuse-lite/data/features/webp.js"
                rem_js: str = "node_modules/caniuse-lite/data/features/rem.js"
                selection_api_js: str = "node_modules/caniuse-lite/data/features/selection-api.js"
                indexeddb2_js: str = "node_modules/caniuse-lite/data/features/indexeddb2.js"
                textcontent_js: str = "node_modules/caniuse-lite/data/features/textcontent.js"
                filereadersync_js: str = "node_modules/caniuse-lite/data/features/filereadersync.js"
                wai_aria_js: str = "node_modules/caniuse-lite/data/features/wai-aria.js"
                dataset_js: str = "node_modules/caniuse-lite/data/features/dataset.js"
                input_selection_js: str = "node_modules/caniuse-lite/data/features/input-selection.js"
                css_lch_lab_js: str = "node_modules/caniuse-lite/data/features/css-lch-lab.js"
                link_rel_modulepreload_js: str = "node_modules/caniuse-lite/data/features/link-rel-modulepreload.js"
                console_time_js: str = "node_modules/caniuse-lite/data/features/console-time.js"
                spdy_js: str = "node_modules/caniuse-lite/data/features/spdy.js"
                array_find_index_js: str = "node_modules/caniuse-lite/data/features/array-find-index.js"
                imagecapture_js: str = "node_modules/caniuse-lite/data/features/imagecapture.js"
                svg_fonts_js: str = "node_modules/caniuse-lite/data/features/svg-fonts.js"
                css_at_counter_style_js: str = "node_modules/caniuse-lite/data/features/css-at-counter-style.js"
                scrollintoview_js: str = "node_modules/caniuse-lite/data/features/scrollintoview.js"
                link_rel_dns_prefetch_js: str = "node_modules/caniuse-lite/data/features/link-rel-dns-prefetch.js"
                forms_js: str = "node_modules/caniuse-lite/data/features/forms.js"
                css_text_spacing_js: str = "node_modules/caniuse-lite/data/features/css-text-spacing.js"
                flexbox_gap_js: str = "node_modules/caniuse-lite/data/features/flexbox-gap.js"
                web_serial_js: str = "node_modules/caniuse-lite/data/features/web-serial.js"
                blobbuilder_js: str = "node_modules/caniuse-lite/data/features/blobbuilder.js"
                av1_js: str = "node_modules/caniuse-lite/data/features/av1.js"
                cors_js: str = "node_modules/caniuse-lite/data/features/cors.js"
                async_clipboard_js: str = "node_modules/caniuse-lite/data/features/async-clipboard.js"
                document_execcommand_js: str = "node_modules/caniuse-lite/data/features/document-execcommand.js"
                user_select_none_js: str = "node_modules/caniuse-lite/data/features/user-select-none.js"
                css_case_insensitive_js: str = "node_modules/caniuse-lite/data/features/css-case-insensitive.js"
                createimagebitmap_js: str = "node_modules/caniuse-lite/data/features/createimagebitmap.js"
                css_first_line_js: str = "node_modules/caniuse-lite/data/features/css-first-line.js"
                constraint_validation_js: str = "node_modules/caniuse-lite/data/features/constraint-validation.js"
                svg_smil_js: str = "node_modules/caniuse-lite/data/features/svg-smil.js"
                channel_messaging_js: str = "node_modules/caniuse-lite/data/features/channel-messaging.js"
                css_unicode_bidi_js: str = "node_modules/caniuse-lite/data/features/css-unicode-bidi.js"
                keyboardevent_key_js: str = "node_modules/caniuse-lite/data/features/keyboardevent-key.js"
                css_dir_pseudo_js: str = "node_modules/caniuse-lite/data/features/css-dir-pseudo.js"
                css_container_queries_js: str = "node_modules/caniuse-lite/data/features/css-container-queries.js"
                input_color_js: str = "node_modules/caniuse-lite/data/features/input-color.js"
                background_img_opts_js: str = "node_modules/caniuse-lite/data/features/background-img-opts.js"
                css_gencontent_js: str = "node_modules/caniuse-lite/data/features/css-gencontent.js"
                insertadjacenthtml_js: str = "node_modules/caniuse-lite/data/features/insertadjacenthtml.js"
                url_js: str = "node_modules/caniuse-lite/data/features/url.js"
                css_resize_js: str = "node_modules/caniuse-lite/data/features/css-resize.js"
                css_featurequeries_js: str = "node_modules/caniuse-lite/data/features/css-featurequeries.js"
                rel_noopener_js: str = "node_modules/caniuse-lite/data/features/rel-noopener.js"
                minmaxwh_js: str = "node_modules/caniuse-lite/data/features/minmaxwh.js"
                matchmedia_js: str = "node_modules/caniuse-lite/data/features/matchmedia.js"
                object_observe_js: str = "node_modules/caniuse-lite/data/features/object-observe.js"
                scrollintoviewifneeded_js: str = "node_modules/caniuse-lite/data/features/scrollintoviewifneeded.js"
                pointer_js: str = "node_modules/caniuse-lite/data/features/pointer.js"
                css_media_scripting_js: str = "node_modules/caniuse-lite/data/features/css-media-scripting.js"
                css_container_queries_style_js: str = "node_modules/caniuse-lite/data/features/css-container-queries-style.js"
                intl_pluralrules_js: str = "node_modules/caniuse-lite/data/features/intl-pluralrules.js"
                input_minlength_js: str = "node_modules/caniuse-lite/data/features/input-minlength.js"
                font_feature_js: str = "node_modules/caniuse-lite/data/features/font-feature.js"
                svg_js: str = "node_modules/caniuse-lite/data/features/svg.js"
                css_caret_color_js: str = "node_modules/caniuse-lite/data/features/css-caret-color.js"
                css_namespaces_js: str = "node_modules/caniuse-lite/data/features/css-namespaces.js"
                webusb_js: str = "node_modules/caniuse-lite/data/features/webusb.js"
                comparedocumentposition_js: str = "node_modules/caniuse-lite/data/features/comparedocumentposition.js"
                webxr_js: str = "node_modules/caniuse-lite/data/features/webxr.js"
                css_image_set_js: str = "node_modules/caniuse-lite/data/features/css-image-set.js"
                css_filters_js: str = "node_modules/caniuse-lite/data/features/css-filters.js"
                url_scroll_to_text_fragment_js: str = "node_modules/caniuse-lite/data/features/url-scroll-to-text-fragment.js"
                meter_js: str = "node_modules/caniuse-lite/data/features/meter.js"
                text_overflow_js: str = "node_modules/caniuse-lite/data/features/text-overflow.js"
                background_position_x_y_js: str = "node_modules/caniuse-lite/data/features/background-position-x-y.js"
                css_widows_orphans_js: str = "node_modules/caniuse-lite/data/features/css-widows-orphans.js"
                template_literals_js: str = "node_modules/caniuse-lite/data/features/template-literals.js"
                picture_js: str = "node_modules/caniuse-lite/data/features/picture.js"
                filesystem_js: str = "node_modules/caniuse-lite/data/features/filesystem.js"
                sql_storage_js: str = "node_modules/caniuse-lite/data/features/sql-storage.js"
                tls1_2_js: str = "node_modules/caniuse-lite/data/features/tls1-2.js"
                namevalue_storage_js: str = "node_modules/caniuse-lite/data/features/namevalue-storage.js"
                wasm_multi_memory_js: str = "node_modules/caniuse-lite/data/features/wasm-multi-memory.js"
                font_smooth_js: str = "node_modules/caniuse-lite/data/features/font-smooth.js"
                document_evaluate_xpath_js: str = "node_modules/caniuse-lite/data/features/document-evaluate-xpath.js"
                webhid_js: str = "node_modules/caniuse-lite/data/features/webhid.js"
                datalist_js: str = "node_modules/caniuse-lite/data/features/datalist.js"
                css_focus_within_js: str = "node_modules/caniuse-lite/data/features/css-focus-within.js"
                fullscreen_js: str = "node_modules/caniuse-lite/data/features/fullscreen.js"
                css_content_visibility_js: str = "node_modules/caniuse-lite/data/features/css-content-visibility.js"
                script_defer_js: str = "node_modules/caniuse-lite/data/features/script-defer.js"
                css_color_function_js: str = "node_modules/caniuse-lite/data/features/css-color-function.js"
                will_change_js: str = "node_modules/caniuse-lite/data/features/will-change.js"
                transforms2d_js: str = "node_modules/caniuse-lite/data/features/transforms2d.js"
                queryselector_js: str = "node_modules/caniuse-lite/data/features/queryselector.js"
                css_autofill_js: str = "node_modules/caniuse-lite/data/features/css-autofill.js"
                object_fit_js: str = "node_modules/caniuse-lite/data/features/object-fit.js"
                xhtmlsmil_js: str = "node_modules/caniuse-lite/data/features/xhtmlsmil.js"
                beforeafterprint_js: str = "node_modules/caniuse-lite/data/features/beforeafterprint.js"
                css_boxdecorationbreak_js: str = "node_modules/caniuse-lite/data/features/css-boxdecorationbreak.js"
                import_maps_js: str = "node_modules/caniuse-lite/data/features/import-maps.js"
                brotli_js: str = "node_modules/caniuse-lite/data/features/brotli.js"
                css_overflow_js: str = "node_modules/caniuse-lite/data/features/css-overflow.js"
                css_indeterminate_pseudo_js: str = "node_modules/caniuse-lite/data/features/css-indeterminate-pseudo.js"
                mdn_css_unicode_bidi_isolate_js: str = "node_modules/caniuse-lite/data/features/mdn-css-unicode-bidi-isolate.js"
                menu_js: str = "node_modules/caniuse-lite/data/features/menu.js"
                css_touch_action_js: str = "node_modules/caniuse-lite/data/features/css-touch-action.js"
                css_media_resolution_js: str = "node_modules/caniuse-lite/data/features/css-media-resolution.js"
                async_functions_js: str = "node_modules/caniuse-lite/data/features/async-functions.js"
                unhandledrejection_js: str = "node_modules/caniuse-lite/data/features/unhandledrejection.js"
                pagevisibility_js: str = "node_modules/caniuse-lite/data/features/pagevisibility.js"
                canvas_text_js: str = "node_modules/caniuse-lite/data/features/canvas-text.js"
                webnfc_js: str = "node_modules/caniuse-lite/data/features/webnfc.js"
                style_scoped_js: str = "node_modules/caniuse-lite/data/features/style-scoped.js"
                ambient_light_js: str = "node_modules/caniuse-lite/data/features/ambient-light.js"
                indexeddb_js: str = "node_modules/caniuse-lite/data/features/indexeddb.js"
                http_live_streaming_js: str = "node_modules/caniuse-lite/data/features/http-live-streaming.js"
                subresource_integrity_js: str = "node_modules/caniuse-lite/data/features/subresource-integrity.js"
                arrow_functions_js: str = "node_modules/caniuse-lite/data/features/arrow-functions.js"
                dom_manip_convenience_js: str = "node_modules/caniuse-lite/data/features/dom-manip-convenience.js"
                css_text_justify_js: str = "node_modules/caniuse-lite/data/features/css-text-justify.js"
                mp3_js: str = "node_modules/caniuse-lite/data/features/mp3.js"
                keyboardevent_getmodifierstate_js: str = "node_modules/caniuse-lite/data/features/keyboardevent-getmodifierstate.js"
                css_unset_value_js: str = "node_modules/caniuse-lite/data/features/css-unset-value.js"
                matchesselector_js: str = "node_modules/caniuse-lite/data/features/matchesselector.js"
                input_file_accept_js: str = "node_modules/caniuse-lite/data/features/input-file-accept.js"
                mdn_text_decoration_shorthand_js: str = "node_modules/caniuse-lite/data/features/mdn-text-decoration-shorthand.js"
                eventsource_js: str = "node_modules/caniuse-lite/data/features/eventsource.js"
                intersectionobserver_v2_js: str = "node_modules/caniuse-lite/data/features/intersectionobserver-v2.js"
                stricttransportsecurity_js: str = "node_modules/caniuse-lite/data/features/stricttransportsecurity.js"
                indeterminate_checkbox_js: str = "node_modules/caniuse-lite/data/features/indeterminate-checkbox.js"
                css_cascade_scope_js: str = "node_modules/caniuse-lite/data/features/css-cascade-scope.js"
                input_email_tel_url_js: str = "node_modules/caniuse-lite/data/features/input-email-tel-url.js"
                css_in_out_of_range_js: str = "node_modules/caniuse-lite/data/features/css-in-out-of-range.js"
                fileapi_js: str = "node_modules/caniuse-lite/data/features/fileapi.js"
                hevc_js: str = "node_modules/caniuse-lite/data/features/hevc.js"
                wasm_simd_js: str = "node_modules/caniuse-lite/data/features/wasm-simd.js"
                proximity_js: str = "node_modules/caniuse-lite/data/features/proximity.js"
                u2f_js: str = "node_modules/caniuse-lite/data/features/u2f.js"
                css_background_offsets_js: str = "node_modules/caniuse-lite/data/features/css-background-offsets.js"
                trusted_types_js: str = "node_modules/caniuse-lite/data/features/trusted-types.js"
                midi_js: str = "node_modules/caniuse-lite/data/features/midi.js"
                asmjs_js: str = "node_modules/caniuse-lite/data/features/asmjs.js"
                wasm_multi_value_js: str = "node_modules/caniuse-lite/data/features/wasm-multi-value.js"
                css3_attr_js: str = "node_modules/caniuse-lite/data/features/css3-attr.js"
                resource_timing_js: str = "node_modules/caniuse-lite/data/features/resource-timing.js"
                document_policy_js: str = "node_modules/caniuse-lite/data/features/document-policy.js"
                webcodecs_js: str = "node_modules/caniuse-lite/data/features/webcodecs.js"
                getelementsbyclassname_js: str = "node_modules/caniuse-lite/data/features/getelementsbyclassname.js"
                css_first_letter_js: str = "node_modules/caniuse-lite/data/features/css-first-letter.js"
                webgl_js: str = "node_modules/caniuse-lite/data/features/webgl.js"
                css_regions_js: str = "node_modules/caniuse-lite/data/features/css-regions.js"
                css_media_interaction_js: str = "node_modules/caniuse-lite/data/features/css-media-interaction.js"
                chacha20_poly1305_js: str = "node_modules/caniuse-lite/data/features/chacha20-poly1305.js"
                setimmediate_js: str = "node_modules/caniuse-lite/data/features/setimmediate.js"
                server_timing_js: str = "node_modules/caniuse-lite/data/features/server-timing.js"
                wordwrap_js: str = "node_modules/caniuse-lite/data/features/wordwrap.js"
                sni_js: str = "node_modules/caniuse-lite/data/features/sni.js"
                css3_cursors_js: str = "node_modules/caniuse-lite/data/features/css3-cursors.js"
                es5_js: str = "node_modules/caniuse-lite/data/features/es5.js"
                css_variables_js: str = "node_modules/caniuse-lite/data/features/css-variables.js"
                css_overflow_anchor_js: str = "node_modules/caniuse-lite/data/features/css-overflow-anchor.js"
                webvr_js: str = "node_modules/caniuse-lite/data/features/webvr.js"
                css_font_rendering_controls_js: str = "node_modules/caniuse-lite/data/features/css-font-rendering-controls.js"
                fieldset_disabled_js: str = "node_modules/caniuse-lite/data/features/fieldset-disabled.js"
                resizeobserver_js: str = "node_modules/caniuse-lite/data/features/resizeobserver.js"
                wasm_gc_js: str = "node_modules/caniuse-lite/data/features/wasm-gc.js"
                videotracks_js: str = "node_modules/caniuse-lite/data/features/videotracks.js"
                css_scroll_behavior_js: str = "node_modules/caniuse-lite/data/features/css-scroll-behavior.js"
                svg_fragment_js: str = "node_modules/caniuse-lite/data/features/svg-fragment.js"
                css_canvas_js: str = "node_modules/caniuse-lite/data/features/css-canvas.js"
                css_print_color_adjust_js: str = "node_modules/caniuse-lite/data/features/css-print-color-adjust.js"
                css_containment_js: str = "node_modules/caniuse-lite/data/features/css-containment.js"
                link_icon_png_js: str = "node_modules/caniuse-lite/data/features/link-icon-png.js"
                es6_string_includes_js: str = "node_modules/caniuse-lite/data/features/es6-string-includes.js"
                devicepixelratio_js: str = "node_modules/caniuse-lite/data/features/devicepixelratio.js"
                clipboard_js: str = "node_modules/caniuse-lite/data/features/clipboard.js"
                css_initial_letter_js: str = "node_modules/caniuse-lite/data/features/css-initial-letter.js"
                json_js: str = "node_modules/caniuse-lite/data/features/json.js"
                passwordrules_js: str = "node_modules/caniuse-lite/data/features/passwordrules.js"
                sdch_js: str = "node_modules/caniuse-lite/data/features/sdch.js"
                websockets_js: str = "node_modules/caniuse-lite/data/features/websockets.js"
                hardwareconcurrency_js: str = "node_modules/caniuse-lite/data/features/hardwareconcurrency.js"
                sharedworkers_js: str = "node_modules/caniuse-lite/data/features/sharedworkers.js"
                css_rebeccapurple_js: str = "node_modules/caniuse-lite/data/features/css-rebeccapurple.js"
                ch_unit_js: str = "node_modules/caniuse-lite/data/features/ch-unit.js"
                transforms3d_js: str = "node_modules/caniuse-lite/data/features/transforms3d.js"
                let_js: str = "node_modules/caniuse-lite/data/features/let.js"
                audio_api_js: str = "node_modules/caniuse-lite/data/features/audio-api.js"
                pdf_viewer_js: str = "node_modules/caniuse-lite/data/features/pdf-viewer.js"
                css_opacity_js: str = "node_modules/caniuse-lite/data/features/css-opacity.js"
                keyboardevent_location_js: str = "node_modules/caniuse-lite/data/features/keyboardevent-location.js"
                link_rel_preload_js: str = "node_modules/caniuse-lite/data/features/link-rel-preload.js"
                apng_js: str = "node_modules/caniuse-lite/data/features/apng.js"
                css_deviceadaptation_js: str = "node_modules/caniuse-lite/data/features/css-deviceadaptation.js"
                once_event_listener_js: str = "node_modules/caniuse-lite/data/features/once-event-listener.js"
                css_line_clamp_js: str = "node_modules/caniuse-lite/data/features/css-line-clamp.js"
                mdn_text_decoration_style_js: str = "node_modules/caniuse-lite/data/features/mdn-text-decoration-style.js"
                justify_content_space_evenly_js: str = "node_modules/caniuse-lite/data/features/justify-content-space-evenly.js"
                gamepad_js: str = "node_modules/caniuse-lite/data/features/gamepad.js"
                pointerlock_js: str = "node_modules/caniuse-lite/data/features/pointerlock.js"
                insert_adjacent_js: str = "node_modules/caniuse-lite/data/features/insert-adjacent.js"
                passkeys_js: str = "node_modules/caniuse-lite/data/features/passkeys.js"
                element_scroll_methods_js: str = "node_modules/caniuse-lite/data/features/element-scroll-methods.js"
                css_counters_js: str = "node_modules/caniuse-lite/data/features/css-counters.js"
                input_file_directory_js: str = "node_modules/caniuse-lite/data/features/input-file-directory.js"
                svg_css_js: str = "node_modules/caniuse-lite/data/features/svg-css.js"
                canvas_blending_js: str = "node_modules/caniuse-lite/data/features/canvas-blending.js"
                addeventlistener_js: str = "node_modules/caniuse-lite/data/features/addeventlistener.js"
                jpegxl_js: str = "node_modules/caniuse-lite/data/features/jpegxl.js"
                domcontentloaded_js: str = "node_modules/caniuse-lite/data/features/domcontentloaded.js"
                wasm_js: str = "node_modules/caniuse-lite/data/features/wasm.js"
                colr_v1_js: str = "node_modules/caniuse-lite/data/features/colr-v1.js"
                eot_js: str = "node_modules/caniuse-lite/data/features/eot.js"
                requestidlecallback_js: str = "node_modules/caniuse-lite/data/features/requestidlecallback.js"
                css_sticky_js: str = "node_modules/caniuse-lite/data/features/css-sticky.js"
                css_page_break_js: str = "node_modules/caniuse-lite/data/features/css-page-break.js"
                page_transition_events_js: str = "node_modules/caniuse-lite/data/features/page-transition-events.js"
                download_js: str = "node_modules/caniuse-lite/data/features/download.js"
                netinfo_js: str = "node_modules/caniuse-lite/data/features/netinfo.js"
                audiotracks_js: str = "node_modules/caniuse-lite/data/features/audiotracks.js"
                user_timing_js: str = "node_modules/caniuse-lite/data/features/user-timing.js"
                client_hints_dpr_width_viewport_js: str = "node_modules/caniuse-lite/data/features/client-hints-dpr-width-viewport.js"
                xml_serializer_js: str = "node_modules/caniuse-lite/data/features/xml-serializer.js"
                requestanimationframe_js: str = "node_modules/caniuse-lite/data/features/requestanimationframe.js"
                input_pattern_js: str = "node_modules/caniuse-lite/data/features/input-pattern.js"
                css_descendant_gtgt_js: str = "node_modules/caniuse-lite/data/features/css-descendant-gtgt.js"
                array_includes_js: str = "node_modules/caniuse-lite/data/features/array-includes.js"
                native_filesystem_api_js: str = "node_modules/caniuse-lite/data/features/native-filesystem-api.js"
                spellcheck_attribute_js: str = "node_modules/caniuse-lite/data/features/spellcheck-attribute.js"
                array_flat_js: str = "node_modules/caniuse-lite/data/features/array-flat.js"
                contentsecuritypolicy_js: str = "node_modules/caniuse-lite/data/features/contentsecuritypolicy.js"
                permissions_policy_js: str = "node_modules/caniuse-lite/data/features/permissions-policy.js"
                css_masks_js: str = "node_modules/caniuse-lite/data/features/css-masks.js"
                offline_apps_js: str = "node_modules/caniuse-lite/data/features/offline-apps.js"
                loading_lazy_attr_js: str = "node_modules/caniuse-lite/data/features/loading-lazy-attr.js"
                css_marker_pseudo_js: str = "node_modules/caniuse-lite/data/features/css-marker-pseudo.js"
                audio_js: str = "node_modules/caniuse-lite/data/features/audio.js"
                css_optional_pseudo_js: str = "node_modules/caniuse-lite/data/features/css-optional-pseudo.js"
                css_element_function_js: str = "node_modules/caniuse-lite/data/features/css-element-function.js"
                css_initial_value_js: str = "node_modules/caniuse-lite/data/features/css-initial-value.js"
                orientation_sensor_js: str = "node_modules/caniuse-lite/data/features/orientation-sensor.js"
                getboundingclientrect_js: str = "node_modules/caniuse-lite/data/features/getboundingclientrect.js"
                rtcpeerconnection_js: str = "node_modules/caniuse-lite/data/features/rtcpeerconnection.js"
                touch_js: str = "node_modules/caniuse-lite/data/features/touch.js"
                imports_js: str = "node_modules/caniuse-lite/data/features/imports.js"
                border_image_js: str = "node_modules/caniuse-lite/data/features/border-image.js"
                progress_js: str = "node_modules/caniuse-lite/data/features/progress.js"
                css_text_align_last_js: str = "node_modules/caniuse-lite/data/features/css-text-align-last.js"
                srcset_js: str = "node_modules/caniuse-lite/data/features/srcset.js"
                svg_img_js: str = "node_modules/caniuse-lite/data/features/svg-img.js"
                dispatchevent_js: str = "node_modules/caniuse-lite/data/features/dispatchevent.js"
                web_share_js: str = "node_modules/caniuse-lite/data/features/web-share.js"
                css_grid_js: str = "node_modules/caniuse-lite/data/features/css-grid.js"
                css_anchor_positioning_js: str = "node_modules/caniuse-lite/data/features/css-anchor-positioning.js"
                css_reflections_js: str = "node_modules/caniuse-lite/data/features/css-reflections.js"
                high_resolution_time_js: str = "node_modules/caniuse-lite/data/features/high-resolution-time.js"
                textencoder_js: str = "node_modules/caniuse-lite/data/features/textencoder.js"
                webauthn_js: str = "node_modules/caniuse-lite/data/features/webauthn.js"
                css3_tabsize_js: str = "node_modules/caniuse-lite/data/features/css3-tabsize.js"
                css_color_adjust_js: str = "node_modules/caniuse-lite/data/features/css-color-adjust.js"
                mutationobserver_js: str = "node_modules/caniuse-lite/data/features/mutationobserver.js"
                wasm_tail_calls_js: str = "node_modules/caniuse-lite/data/features/wasm-tail-calls.js"
                hidden_js: str = "node_modules/caniuse-lite/data/features/hidden.js"
                css_supports_api_js: str = "node_modules/caniuse-lite/data/features/css-supports-api.js"
                css_image_orientation_js: str = "node_modules/caniuse-lite/data/features/css-image-orientation.js"
                meta_theme_color_js: str = "node_modules/caniuse-lite/data/features/meta-theme-color.js"
                shadowdom_js: str = "node_modules/caniuse-lite/data/features/shadowdom.js"
                es6_module_js: str = "node_modules/caniuse-lite/data/features/es6-module.js"
                ogg_vorbis_js: str = "node_modules/caniuse-lite/data/features/ogg-vorbis.js"
                console_basic_js: str = "node_modules/caniuse-lite/data/features/console-basic.js"
                view_transitions_js: str = "node_modules/caniuse-lite/data/features/view-transitions.js"
                mediasource_js: str = "node_modules/caniuse-lite/data/features/mediasource.js"
                css_boxshadow_js: str = "node_modules/caniuse-lite/data/features/css-boxshadow.js"
                css_has_js: str = "node_modules/caniuse-lite/data/features/css-has.js"
                css_logical_props_js: str = "node_modules/caniuse-lite/data/features/css-logical-props.js"
                abortcontroller_js: str = "node_modules/caniuse-lite/data/features/abortcontroller.js"
                webtransport_js: str = "node_modules/caniuse-lite/data/features/webtransport.js"
                wasm_signext_js: str = "node_modules/caniuse-lite/data/features/wasm-signext.js"
                speech_synthesis_js: str = "node_modules/caniuse-lite/data/features/speech-synthesis.js"
                text_size_adjust_js: str = "node_modules/caniuse-lite/data/features/text-size-adjust.js"
                wasm_relaxed_simd_js: str = "node_modules/caniuse-lite/data/features/wasm-relaxed-simd.js"
                ruby_js: str = "node_modules/caniuse-lite/data/features/ruby.js"
                offscreencanvas_js: str = "node_modules/caniuse-lite/data/features/offscreencanvas.js"
                css3_boxsizing_js: str = "node_modules/caniuse-lite/data/features/css3-boxsizing.js"
                urlsearchparams_js: str = "node_modules/caniuse-lite/data/features/urlsearchparams.js"
                multicolumn_js: str = "node_modules/caniuse-lite/data/features/multicolumn.js"
                filereader_js: str = "node_modules/caniuse-lite/data/features/filereader.js"
                css_shapes_js: str = "node_modules/caniuse-lite/data/features/css-shapes.js"
                wasm_bigint_js: str = "node_modules/caniuse-lite/data/features/wasm-bigint.js"
                localecompare_js: str = "node_modules/caniuse-lite/data/features/localecompare.js"
                bloburls_js: str = "node_modules/caniuse-lite/data/features/bloburls.js"
                webworkers_js: str = "node_modules/caniuse-lite/data/features/webworkers.js"
                upgradeinsecurerequests_js: str = "node_modules/caniuse-lite/data/features/upgradeinsecurerequests.js"
                css_textshadow_js: str = "node_modules/caniuse-lite/data/features/css-textshadow.js"
                css_width_stretch_js: str = "node_modules/caniuse-lite/data/features/css-width-stretch.js"
                gyroscope_js: str = "node_modules/caniuse-lite/data/features/gyroscope.js"
                aac_js: str = "node_modules/caniuse-lite/data/features/aac.js"
                path2d_js: str = "node_modules/caniuse-lite/data/features/path2d.js"
                heif_js: str = "node_modules/caniuse-lite/data/features/heif.js"
                zstd_js: str = "node_modules/caniuse-lite/data/features/zstd.js"
                stream_js: str = "node_modules/caniuse-lite/data/features/stream.js"
                css_mediaqueries_js: str = "node_modules/caniuse-lite/data/features/css-mediaqueries.js"
                document_currentscript_js: str = "node_modules/caniuse-lite/data/features/document-currentscript.js"
                css_paint_api_js: str = "node_modules/caniuse-lite/data/features/css-paint-api.js"
                viewport_units_js: str = "node_modules/caniuse-lite/data/features/viewport-units.js"
                form_attribute_js: str = "node_modules/caniuse-lite/data/features/form-attribute.js"
                mdn_css_unicode_bidi_plaintext_js: str = "node_modules/caniuse-lite/data/features/mdn-css-unicode-bidi-plaintext.js"
                geolocation_js: str = "node_modules/caniuse-lite/data/features/geolocation.js"
                wake_lock_js: str = "node_modules/caniuse-lite/data/features/wake-lock.js"
                css_text_wrap_balance_js: str = "node_modules/caniuse-lite/data/features/css-text-wrap-balance.js"
                webm_js: str = "node_modules/caniuse-lite/data/features/webm.js"
                css_when_else_js: str = "node_modules/caniuse-lite/data/features/css-when-else.js"
                maxlength_js: str = "node_modules/caniuse-lite/data/features/maxlength.js"
                object_values_js: str = "node_modules/caniuse-lite/data/features/object-values.js"
                outline_js: str = "node_modules/caniuse-lite/data/features/outline.js"
                mutation_events_js: str = "node_modules/caniuse-lite/data/features/mutation-events.js"
                woff_js: str = "node_modules/caniuse-lite/data/features/woff.js"
                prefers_reduced_motion_js: str = "node_modules/caniuse-lite/data/features/prefers-reduced-motion.js"
                css_cascade_layers_js: str = "node_modules/caniuse-lite/data/features/css-cascade-layers.js"
                link_icon_svg_js: str = "node_modules/caniuse-lite/data/features/link-icon-svg.js"
                img_naturalwidth_naturalheight_js: str = "node_modules/caniuse-lite/data/features/img-naturalwidth-naturalheight.js"
                credential_management_js: str = "node_modules/caniuse-lite/data/features/credential-management.js"
                documenthead_js: str = "node_modules/caniuse-lite/data/features/documenthead.js"
                contentsecuritypolicy2_js: str = "node_modules/caniuse-lite/data/features/contentsecuritypolicy2.js"
                web_bluetooth_js: str = "node_modules/caniuse-lite/data/features/web-bluetooth.js"
                font_unicode_range_js: str = "node_modules/caniuse-lite/data/features/font-unicode-range.js"
                background_clip_text_js: str = "node_modules/caniuse-lite/data/features/background-clip-text.js"
                css_any_link_js: str = "node_modules/caniuse-lite/data/features/css-any-link.js"
                same_site_cookie_attribute_js: str = "node_modules/caniuse-lite/data/features/same-site-cookie-attribute.js"
                css_selection_js: str = "node_modules/caniuse-lite/data/features/css-selection.js"
                autofocus_js: str = "node_modules/caniuse-lite/data/features/autofocus.js"
                tls1_1_js: str = "node_modules/caniuse-lite/data/features/tls1-1.js"
                decorators_js: str = "node_modules/caniuse-lite/data/features/decorators.js"
                tabindex_attr_js: str = "node_modules/caniuse-lite/data/features/tabindex-attr.js"
                sxg_js: str = "node_modules/caniuse-lite/data/features/sxg.js"
                background_attachment_js: str = "node_modules/caniuse-lite/data/features/background-attachment.js"
                html5semantic_js: str = "node_modules/caniuse-lite/data/features/html5semantic.js"
                css_exclusions_js: str = "node_modules/caniuse-lite/data/features/css-exclusions.js"
                getcomputedstyle_js: str = "node_modules/caniuse-lite/data/features/getcomputedstyle.js"
                css_table_js: str = "node_modules/caniuse-lite/data/features/css-table.js"
                element_closest_js: str = "node_modules/caniuse-lite/data/features/element-closest.js"
                colr_js: str = "node_modules/caniuse-lite/data/features/colr.js"
                tls1_3_js: str = "node_modules/caniuse-lite/data/features/tls1-3.js"
                css_font_palette_js: str = "node_modules/caniuse-lite/data/features/css-font-palette.js"
                dnssec_js: str = "node_modules/caniuse-lite/data/features/dnssec.js"
                css_transitions_js: str = "node_modules/caniuse-lite/data/features/css-transitions.js"
                dragndrop_js: str = "node_modules/caniuse-lite/data/features/dragndrop.js"
                form_submit_attributes_js: str = "node_modules/caniuse-lite/data/features/form-submit-attributes.js"
                css_conic_gradients_js: str = "node_modules/caniuse-lite/data/features/css-conic-gradients.js"
                intersectionobserver_js: str = "node_modules/caniuse-lite/data/features/intersectionobserver.js"
                css_subgrid_js: str = "node_modules/caniuse-lite/data/features/css-subgrid.js"
                run_in_js: str = "node_modules/caniuse-lite/data/features/run-in.js"
                avif_js: str = "node_modules/caniuse-lite/data/features/avif.js"
                streams_js: str = "node_modules/caniuse-lite/data/features/streams.js"
                publickeypinning_js: str = "node_modules/caniuse-lite/data/features/publickeypinning.js"
                vector_effect_js: str = "node_modules/caniuse-lite/data/features/vector-effect.js"
                declarative_shadow_dom_js: str = "node_modules/caniuse-lite/data/features/declarative-shadow-dom.js"
                css_nesting_js: str = "node_modules/caniuse-lite/data/features/css-nesting.js"
                css_grid_animation_js: str = "node_modules/caniuse-lite/data/features/css-grid-animation.js"
                css_mixblendmode_js: str = "node_modules/caniuse-lite/data/features/css-mixblendmode.js"
                do_not_track_js: str = "node_modules/caniuse-lite/data/features/do-not-track.js"
                css_writing_mode_js: str = "node_modules/caniuse-lite/data/features/css-writing-mode.js"
                css_revert_value_js: str = "node_modules/caniuse-lite/data/features/css-revert-value.js"
                css_placeholder_js: str = "node_modules/caniuse-lite/data/features/css-placeholder.js"
                css_matches_pseudo_js: str = "node_modules/caniuse-lite/data/features/css-matches-pseudo.js"
                css_scrollbar_js: str = "node_modules/caniuse-lite/data/features/css-scrollbar.js"
                background_sync_js: str = "node_modules/caniuse-lite/data/features/background-sync.js"
                webgl2_js: str = "node_modules/caniuse-lite/data/features/webgl2.js"
                svg_html_js: str = "node_modules/caniuse-lite/data/features/svg-html.js"
                border_radius_js: str = "node_modules/caniuse-lite/data/features/border-radius.js"
                jpeg2000_js: str = "node_modules/caniuse-lite/data/features/jpeg2000.js"
                wav_js: str = "node_modules/caniuse-lite/data/features/wav.js"
                css_gradients_js: str = "node_modules/caniuse-lite/data/features/css-gradients.js"
                css_rrggbbaa_js: str = "node_modules/caniuse-lite/data/features/css-rrggbbaa.js"
                text_decoration_js: str = "node_modules/caniuse-lite/data/features/text-decoration.js"
                css_backdrop_filter_js: str = "node_modules/caniuse-lite/data/features/css-backdrop-filter.js"
                speech_recognition_js: str = "node_modules/caniuse-lite/data/features/speech-recognition.js"
                css_crisp_edges_js: str = "node_modules/caniuse-lite/data/features/css-crisp-edges.js"
                text_stroke_js: str = "node_modules/caniuse-lite/data/features/text-stroke.js"
                x_frame_options_js: str = "node_modules/caniuse-lite/data/features/x-frame-options.js"
                css_text_box_trim_js: str = "node_modules/caniuse-lite/data/features/css-text-box-trim.js"
                flexbox_js: str = "node_modules/caniuse-lite/data/features/flexbox.js"
                screen_orientation_js: str = "node_modules/caniuse-lite/data/features/screen-orientation.js"
                css_animation_js: str = "node_modules/caniuse-lite/data/features/css-animation.js"
                eme_js: str = "node_modules/caniuse-lite/data/features/eme.js"
                html_media_capture_js: str = "node_modules/caniuse-lite/data/features/html-media-capture.js"
                const_js: str = "node_modules/caniuse-lite/data/features/const.js"
                link_rel_preconnect_js: str = "node_modules/caniuse-lite/data/features/link-rel-preconnect.js"
                innertext_js: str = "node_modules/caniuse-lite/data/features/innertext.js"
                css_placeholder_shown_js: str = "node_modules/caniuse-lite/data/features/css-placeholder-shown.js"
                promise_finally_js: str = "node_modules/caniuse-lite/data/features/promise-finally.js"
                classlist_js: str = "node_modules/caniuse-lite/data/features/classlist.js"
                css_motion_paths_js: str = "node_modules/caniuse-lite/data/features/css-motion-paths.js"
                css3_cursors_grab_js: str = "node_modules/caniuse-lite/data/features/css3-cursors-grab.js"
                media_fragments_js: str = "node_modules/caniuse-lite/data/features/media-fragments.js"
                css_module_scripts_js: str = "node_modules/caniuse-lite/data/features/css-module-scripts.js"
                keyboardevent_charcode_js: str = "node_modules/caniuse-lite/data/features/keyboardevent-charcode.js"
                iframe_sandbox_js: str = "node_modules/caniuse-lite/data/features/iframe-sandbox.js"
                css_fixed_js: str = "node_modules/caniuse-lite/data/features/css-fixed.js"
                css_sel2_js: str = "node_modules/caniuse-lite/data/features/css-sel2.js"
                font_variant_numeric_js: str = "node_modules/caniuse-lite/data/features/font-variant-numeric.js"
                wasm_threads_js: str = "node_modules/caniuse-lite/data/features/wasm-threads.js"
                wasm_nontrapping_fptoint_js: str = "node_modules/caniuse-lite/data/features/wasm-nontrapping-fptoint.js"
                portals_js: str = "node_modules/caniuse-lite/data/features/portals.js"
                input_file_multiple_js: str = "node_modules/caniuse-lite/data/features/input-file-multiple.js"
                css_hyphens_js: str = "node_modules/caniuse-lite/data/features/css-hyphens.js"
                wbr_element_js: str = "node_modules/caniuse-lite/data/features/wbr-element.js"
                custom_elementsv1_js: str = "node_modules/caniuse-lite/data/features/custom-elementsv1.js"
                datauri_js: str = "node_modules/caniuse-lite/data/features/datauri.js"
                css_hanging_punctuation_js: str = "node_modules/caniuse-lite/data/features/css-hanging-punctuation.js"
                dommatrix_js: str = "node_modules/caniuse-lite/data/features/dommatrix.js"
                fetch_js: str = "node_modules/caniuse-lite/data/features/fetch.js"
                mdn_css_unicode_bidi_isolate_override_js: str = "node_modules/caniuse-lite/data/features/mdn-css-unicode-bidi-isolate-override.js"
                wasm_mutable_globals_js: str = "node_modules/caniuse-lite/data/features/wasm-mutable-globals.js"
                web_app_manifest_js: str = "node_modules/caniuse-lite/data/features/web-app-manifest.js"
                ping_js: str = "node_modules/caniuse-lite/data/features/ping.js"
                input_number_js: str = "node_modules/caniuse-lite/data/features/input-number.js"
                css_cross_fade_js: str = "node_modules/caniuse-lite/data/features/css-cross-fade.js"
                es6_class_js: str = "node_modules/caniuse-lite/data/features/es6-class.js"
                object_entries_js: str = "node_modules/caniuse-lite/data/features/object-entries.js"
                font_loading_js: str = "node_modules/caniuse-lite/data/features/font-loading.js"
                x_doc_messaging_js: str = "node_modules/caniuse-lite/data/features/x-doc-messaging.js"
                css_not_sel_list_js: str = "node_modules/caniuse-lite/data/features/css-not-sel-list.js"
                mediacapture_fromelement_js: str = "node_modules/caniuse-lite/data/features/mediacapture-fromelement.js"
                mdn_text_decoration_color_js: str = "node_modules/caniuse-lite/data/features/mdn-text-decoration-color.js"
                css_file_selector_button_js: str = "node_modules/caniuse-lite/data/features/css-file-selector-button.js"
                currentcolor_js: str = "node_modules/caniuse-lite/data/features/currentcolor.js"
                xhtml_js: str = "node_modules/caniuse-lite/data/features/xhtml.js"
                document_scrollingelement_js: str = "node_modules/caniuse-lite/data/features/document-scrollingelement.js"
                sharedarraybuffer_js: str = "node_modules/caniuse-lite/data/features/sharedarraybuffer.js"
                ac3_ec3_js: str = "node_modules/caniuse-lite/data/features/ac3-ec3.js"
                feature_policy_js: str = "node_modules/caniuse-lite/data/features/feature-policy.js"
                input_inputmode_js: str = "node_modules/caniuse-lite/data/features/input-inputmode.js"
                mediarecorder_js: str = "node_modules/caniuse-lite/data/features/mediarecorder.js"
                serviceworkers_js: str = "node_modules/caniuse-lite/data/features/serviceworkers.js"
                objectrtc_js: str = "node_modules/caniuse-lite/data/features/objectrtc.js"
                http2_js: str = "node_modules/caniuse-lite/data/features/http2.js"
                custom_elements_js: str = "node_modules/caniuse-lite/data/features/custom-elements.js"
                keyboardevent_which_js: str = "node_modules/caniuse-lite/data/features/keyboardevent-which.js"
                calc_js: str = "node_modules/caniuse-lite/data/features/calc.js"
                nav_timing_js: str = "node_modules/caniuse-lite/data/features/nav-timing.js"
                css_text_orientation_js: str = "node_modules/caniuse-lite/data/features/css-text-orientation.js"
                extended_system_fonts_js: str = "node_modules/caniuse-lite/data/features/extended-system-fonts.js"
                alternate_stylesheet_js: str = "node_modules/caniuse-lite/data/features/alternate-stylesheet.js"
                wasm_reference_types_js: str = "node_modules/caniuse-lite/data/features/wasm-reference-types.js"
                input_event_js: str = "node_modules/caniuse-lite/data/features/input-event.js"
                permissions_api_js: str = "node_modules/caniuse-lite/data/features/permissions-api.js"
                typedarrays_js: str = "node_modules/caniuse-lite/data/features/typedarrays.js"
                pointer_events_js: str = "node_modules/caniuse-lite/data/features/pointer-events.js"
                temporal_js: str = "node_modules/caniuse-lite/data/features/temporal.js"
                fontface_js: str = "node_modules/caniuse-lite/data/features/fontface.js"
                mpeg4_js: str = "node_modules/caniuse-lite/data/features/mpeg4.js"
                css_overflow_overlay_js: str = "node_modules/caniuse-lite/data/features/css-overflow-overlay.js"
                internationalization_js: str = "node_modules/caniuse-lite/data/features/internationalization.js"
                customevent_js: str = "node_modules/caniuse-lite/data/features/customevent.js"
                ttf_js: str = "node_modules/caniuse-lite/data/features/ttf.js"
                flow_root_js: str = "node_modules/caniuse-lite/data/features/flow-root.js"
                rest_parameters_js: str = "node_modules/caniuse-lite/data/features/rest-parameters.js"
                referrer_policy_js: str = "node_modules/caniuse-lite/data/features/referrer-policy.js"
                css_container_query_units_js: str = "node_modules/caniuse-lite/data/features/css-container-query-units.js"
                css_backgroundblendmode_js: str = "node_modules/caniuse-lite/data/features/css-backgroundblendmode.js"
                css_snappoints_js: str = "node_modules/caniuse-lite/data/features/css-snappoints.js"
                cryptography_js: str = "node_modules/caniuse-lite/data/features/cryptography.js"
            features = _node_modules_caniuse_lite_data_features()
        data = _node_modules_caniuse_lite_data()
    caniuse_lite = _node_modules_caniuse_lite()
    p_finally: str = "node_modules/p-finally/index.js"
    object_assign: str = "node_modules/object-assign/index.js"
    thenify_all: str = "node_modules/thenify-all/index.js"

    class _node_modules_postcss_svgo:

        class _node_modules_postcss_svgo_src:
            index_js: str = "node_modules/postcss-svgo/src/index.js"
            lib: str = "node_modules/postcss-svgo/src/lib/url.js"
        src = _node_modules_postcss_svgo_src()
    postcss_svgo = _node_modules_postcss_svgo()

    class _node_modules_electron_to_chromium:
        index_js: str = "node_modules/electron-to-chromium/index.js"
        chromium_versions_js: str = "node_modules/electron-to-chromium/chromium-versions.js"
        full_versions_js: str = "node_modules/electron-to-chromium/full-versions.js"
        versions_js: str = "node_modules/electron-to-chromium/versions.js"
        full_chromium_versions_js: str = "node_modules/electron-to-chromium/full-chromium-versions.js"
    electron_to_chromium = _node_modules_electron_to_chromium()

    class _node_modules_postcss_normalize_positions:
        src: str = "node_modules/postcss-normalize-positions/src/index.js"
    postcss_normalize_positions = _node_modules_postcss_normalize_positions()

    class _node_modules_object_hash:
        index_js: str = "node_modules/object-hash/index.js"
        dist: str = "node_modules/object-hash/dist/object_hash.js"
    object_hash = _node_modules_object_hash()

    class _node_modules_chokidar:
        index_js: str = "node_modules/chokidar/index.js"

        class _node_modules_chokidar_node_modules:
            glob_parent: str = "node_modules/chokidar/node_modules/glob-parent/index.js"
        node_modules = _node_modules_chokidar_node_modules()

        class _node_modules_chokidar_lib:
            constants_js: str = "node_modules/chokidar/lib/constants.js"
            nodefs_handler_js: str = "node_modules/chokidar/lib/nodefs-handler.js"
            fsevents_handler_js: str = "node_modules/chokidar/lib/fsevents-handler.js"
        lib = _node_modules_chokidar_lib()
    chokidar = _node_modules_chokidar()
    binary_extensions: str = "node_modules/binary-extensions/index.js"
    boolbase: str = "node_modules/boolbase/index.js"

    class _node_modules_pirates:
        lib: str = "node_modules/pirates/lib/index.js"
    pirates = _node_modules_pirates()

    class _node_modules_supports_color:
        index_js: str = "node_modules/supports-color/index.js"
        browser_js: str = "node_modules/supports-color/browser.js"
    supports_color = _node_modules_supports_color()
    eastasianwidth: str = "node_modules/eastasianwidth/eastasianwidth.js"
    shebang_regex: str = "node_modules/shebang-regex/index.js"

    class _node_modules_css_tree:

        class _node_modules_css_tree_lib:
            index_js: str = "node_modules/css-tree/lib/index.js"

            class _node_modules_css_tree_lib_utils:
                names_js: str = "node_modules/css-tree/lib/utils/names.js"
                clone_js: str = "node_modules/css-tree/lib/utils/clone.js"
                createCustomError_js: str = "node_modules/css-tree/lib/utils/createCustomError.js"
            utils = _node_modules_css_tree_lib_utils()

            class _node_modules_css_tree_lib_walker:
                index_js: str = "node_modules/css-tree/lib/walker/index.js"
                create_js: str = "node_modules/css-tree/lib/walker/create.js"
            walker = _node_modules_css_tree_lib_walker()

            class _node_modules_css_tree_lib_generator:
                sourceMap_js: str = "node_modules/css-tree/lib/generator/sourceMap.js"
                index_js: str = "node_modules/css-tree/lib/generator/index.js"
                create_js: str = "node_modules/css-tree/lib/generator/create.js"
            generator = _node_modules_css_tree_lib_generator()

            class _node_modules_css_tree_lib_convertor:
                index_js: str = "node_modules/css-tree/lib/convertor/index.js"
                create_js: str = "node_modules/css-tree/lib/convertor/create.js"
            convertor = _node_modules_css_tree_lib_convertor()

            class _node_modules_css_tree_lib_common:
                adopt_buffer_js: str = "node_modules/css-tree/lib/common/adopt-buffer.js"
                TokenStream_js: str = "node_modules/css-tree/lib/common/TokenStream.js"
                List_js: str = "node_modules/css-tree/lib/common/List.js"
                OffsetToLocation_js: str = "node_modules/css-tree/lib/common/OffsetToLocation.js"
                SyntaxError_js: str = "node_modules/css-tree/lib/common/SyntaxError.js"
            common = _node_modules_css_tree_lib_common()

            class _node_modules_css_tree_lib_parser:
                index_js: str = "node_modules/css-tree/lib/parser/index.js"
                sequence_js: str = "node_modules/css-tree/lib/parser/sequence.js"
                create_js: str = "node_modules/css-tree/lib/parser/create.js"
            parser = _node_modules_css_tree_lib_parser()

            class _node_modules_css_tree_lib_tokenizer:
                utils_js: str = "node_modules/css-tree/lib/tokenizer/utils.js"
                index_js: str = "node_modules/css-tree/lib/tokenizer/index.js"
                char_code_definitions_js: str = "node_modules/css-tree/lib/tokenizer/char-code-definitions.js"
                const_js: str = "node_modules/css-tree/lib/tokenizer/const.js"
            tokenizer = _node_modules_css_tree_lib_tokenizer()

            class _node_modules_css_tree_lib_lexer:
                generic_urange_js: str = "node_modules/css-tree/lib/lexer/generic-urange.js"
                trace_js: str = "node_modules/css-tree/lib/lexer/trace.js"
                index_js: str = "node_modules/css-tree/lib/lexer/index.js"
                structure_js: str = "node_modules/css-tree/lib/lexer/structure.js"
                generic_js: str = "node_modules/css-tree/lib/lexer/generic.js"
                prepare_tokens_js: str = "node_modules/css-tree/lib/lexer/prepare-tokens.js"
                Lexer_js: str = "node_modules/css-tree/lib/lexer/Lexer.js"
                match_js: str = "node_modules/css-tree/lib/lexer/match.js"
                error_js: str = "node_modules/css-tree/lib/lexer/error.js"
                match_graph_js: str = "node_modules/css-tree/lib/lexer/match-graph.js"
                generic_an_plus_b_js: str = "node_modules/css-tree/lib/lexer/generic-an-plus-b.js"
                search_js: str = "node_modules/css-tree/lib/lexer/search.js"
            lexer = _node_modules_css_tree_lib_lexer()

            class _node_modules_css_tree_lib_definition_syntax:
                parse_js: str = "node_modules/css-tree/lib/definition-syntax/parse.js"
                walk_js: str = "node_modules/css-tree/lib/definition-syntax/walk.js"
                index_js: str = "node_modules/css-tree/lib/definition-syntax/index.js"
                tokenizer_js: str = "node_modules/css-tree/lib/definition-syntax/tokenizer.js"
                SyntaxError_js: str = "node_modules/css-tree/lib/definition-syntax/SyntaxError.js"
                generate_js: str = "node_modules/css-tree/lib/definition-syntax/generate.js"
            definition_syntax = _node_modules_css_tree_lib_definition_syntax()

            class _node_modules_css_tree_lib_syntax:
                index_js: str = "node_modules/css-tree/lib/syntax/index.js"
                create_js: str = "node_modules/css-tree/lib/syntax/create.js"

                class _node_modules_css_tree_lib_syntax_scope:
                    value_js: str = "node_modules/css-tree/lib/syntax/scope/value.js"
                    index_js: str = "node_modules/css-tree/lib/syntax/scope/index.js"
                    atrulePrelude_js: str = "node_modules/css-tree/lib/syntax/scope/atrulePrelude.js"
                    default_js: str = "node_modules/css-tree/lib/syntax/scope/default.js"
                    selector_js: str = "node_modules/css-tree/lib/syntax/scope/selector.js"
                scope = _node_modules_css_tree_lib_syntax_scope()

                class _node_modules_css_tree_lib_syntax_atrule:
                    font_face_js: str = "node_modules/css-tree/lib/syntax/atrule/font-face.js"
                    import_js: str = "node_modules/css-tree/lib/syntax/atrule/import.js"
                    page_js: str = "node_modules/css-tree/lib/syntax/atrule/page.js"
                    index_js: str = "node_modules/css-tree/lib/syntax/atrule/index.js"
                    media_js: str = "node_modules/css-tree/lib/syntax/atrule/media.js"
                    supports_js: str = "node_modules/css-tree/lib/syntax/atrule/supports.js"
                atrule = _node_modules_css_tree_lib_syntax_atrule()

                class _node_modules_css_tree_lib_syntax_config:
                    walker_js: str = "node_modules/css-tree/lib/syntax/config/walker.js"
                    parser_js: str = "node_modules/css-tree/lib/syntax/config/parser.js"
                    mix_js: str = "node_modules/css-tree/lib/syntax/config/mix.js"
                    lexer_js: str = "node_modules/css-tree/lib/syntax/config/lexer.js"
                config = _node_modules_css_tree_lib_syntax_config()

                class _node_modules_css_tree_lib_syntax_pseudo:
                    nth_of_type_js: str = "node_modules/css-tree/lib/syntax/pseudo/nth-of-type.js"
                    not_js: str = "node_modules/css-tree/lib/syntax/pseudo/not.js"
                    nth_child_js: str = "node_modules/css-tree/lib/syntax/pseudo/nth-child.js"
                    has_js: str = "node_modules/css-tree/lib/syntax/pseudo/has.js"
                    slotted_js: str = "node_modules/css-tree/lib/syntax/pseudo/slotted.js"
                    index_js: str = "node_modules/css-tree/lib/syntax/pseudo/index.js"
                    dir_js: str = "node_modules/css-tree/lib/syntax/pseudo/dir.js"
                    lang_js: str = "node_modules/css-tree/lib/syntax/pseudo/lang.js"
                    nth_last_child_js: str = "node_modules/css-tree/lib/syntax/pseudo/nth-last-child.js"
                    nth_last_of_type_js: str = "node_modules/css-tree/lib/syntax/pseudo/nth-last-of-type.js"
                    matches_js: str = "node_modules/css-tree/lib/syntax/pseudo/matches.js"

                    class _node_modules_css_tree_lib_syntax_pseudo_common:
                        nth_js: str = "node_modules/css-tree/lib/syntax/pseudo/common/nth.js"
                        selectorList_js: str = "node_modules/css-tree/lib/syntax/pseudo/common/selectorList.js"
                        nthWithOfClause_js: str = "node_modules/css-tree/lib/syntax/pseudo/common/nthWithOfClause.js"
                    common = _node_modules_css_tree_lib_syntax_pseudo_common()
                pseudo = _node_modules_css_tree_lib_syntax_pseudo()

                class _node_modules_css_tree_lib_syntax_node:
                    Operator_js: str = "node_modules/css-tree/lib/syntax/node/Operator.js"
                    Combinator_js: str = "node_modules/css-tree/lib/syntax/node/Combinator.js"
                    CDO_js: str = "node_modules/css-tree/lib/syntax/node/CDO.js"
                    Url_js: str = "node_modules/css-tree/lib/syntax/node/Url.js"
                    Value_js: str = "node_modules/css-tree/lib/syntax/node/Value.js"
                    AnPlusB_js: str = "node_modules/css-tree/lib/syntax/node/AnPlusB.js"
                    Ratio_js: str = "node_modules/css-tree/lib/syntax/node/Ratio.js"
                    MediaQuery_js: str = "node_modules/css-tree/lib/syntax/node/MediaQuery.js"
                    Identifier_js: str = "node_modules/css-tree/lib/syntax/node/Identifier.js"
                    TypeSelector_js: str = "node_modules/css-tree/lib/syntax/node/TypeSelector.js"
                    String_js: str = "node_modules/css-tree/lib/syntax/node/String.js"
                    Number_js: str = "node_modules/css-tree/lib/syntax/node/Number.js"
                    AtrulePrelude_js: str = "node_modules/css-tree/lib/syntax/node/AtrulePrelude.js"
                    Selector_js: str = "node_modules/css-tree/lib/syntax/node/Selector.js"
                    IdSelector_js: str = "node_modules/css-tree/lib/syntax/node/IdSelector.js"
                    Percentage_js: str = "node_modules/css-tree/lib/syntax/node/Percentage.js"
                    MediaFeature_js: str = "node_modules/css-tree/lib/syntax/node/MediaFeature.js"
                    MediaQueryList_js: str = "node_modules/css-tree/lib/syntax/node/MediaQueryList.js"
                    Raw_js: str = "node_modules/css-tree/lib/syntax/node/Raw.js"
                    CDC_js: str = "node_modules/css-tree/lib/syntax/node/CDC.js"
                    index_js: str = "node_modules/css-tree/lib/syntax/node/index.js"
                    Block_js: str = "node_modules/css-tree/lib/syntax/node/Block.js"
                    Atrule_js: str = "node_modules/css-tree/lib/syntax/node/Atrule.js"
                    Dimension_js: str = "node_modules/css-tree/lib/syntax/node/Dimension.js"
                    Brackets_js: str = "node_modules/css-tree/lib/syntax/node/Brackets.js"
                    Hash_js: str = "node_modules/css-tree/lib/syntax/node/Hash.js"
                    ClassSelector_js: str = "node_modules/css-tree/lib/syntax/node/ClassSelector.js"
                    Declaration_js: str = "node_modules/css-tree/lib/syntax/node/Declaration.js"
                    Function_js: str = "node_modules/css-tree/lib/syntax/node/Function.js"
                    PseudoElementSelector_js: str = "node_modules/css-tree/lib/syntax/node/PseudoElementSelector.js"
                    AttributeSelector_js: str = "node_modules/css-tree/lib/syntax/node/AttributeSelector.js"
                    PseudoClassSelector_js: str = "node_modules/css-tree/lib/syntax/node/PseudoClassSelector.js"
                    StyleSheet_js: str = "node_modules/css-tree/lib/syntax/node/StyleSheet.js"
                    Rule_js: str = "node_modules/css-tree/lib/syntax/node/Rule.js"
                    Nth_js: str = "node_modules/css-tree/lib/syntax/node/Nth.js"
                    Comment_js: str = "node_modules/css-tree/lib/syntax/node/Comment.js"
                    UnicodeRange_js: str = "node_modules/css-tree/lib/syntax/node/UnicodeRange.js"
                    WhiteSpace_js: str = "node_modules/css-tree/lib/syntax/node/WhiteSpace.js"
                    Parentheses_js: str = "node_modules/css-tree/lib/syntax/node/Parentheses.js"
                    SelectorList_js: str = "node_modules/css-tree/lib/syntax/node/SelectorList.js"
                    DeclarationList_js: str = "node_modules/css-tree/lib/syntax/node/DeclarationList.js"
                node = _node_modules_css_tree_lib_syntax_node()

                class _node_modules_css_tree_lib_syntax_function:
                    expression_js: str = "node_modules/css-tree/lib/syntax/function/expression.js"
                    var_js: str = "node_modules/css-tree/lib/syntax/function/var.js"
                function = _node_modules_css_tree_lib_syntax_function()
            syntax = _node_modules_css_tree_lib_syntax()
        lib = _node_modules_css_tree_lib()

        class _node_modules_css_tree_dist:
            csstree_js: str = "node_modules/css-tree/dist/csstree.js"
            csstree_min_js: str = "node_modules/css-tree/dist/csstree.min.js"
        dist = _node_modules_css_tree_dist()
        data: str = "node_modules/css-tree/data/index.js"
    css_tree = _node_modules_css_tree()

    class _node_modules_postcss_ordered_values:

        class _node_modules_postcss_ordered_values_src:
            index_js: str = "node_modules/postcss-ordered-values/src/index.js"

            class _node_modules_postcss_ordered_values_src_lib:
                getValue_js: str = "node_modules/postcss-ordered-values/src/lib/getValue.js"
                mathfunctions_js: str = "node_modules/postcss-ordered-values/src/lib/mathfunctions.js"
                addSpace_js: str = "node_modules/postcss-ordered-values/src/lib/addSpace.js"
                vendorUnprefixed_js: str = "node_modules/postcss-ordered-values/src/lib/vendorUnprefixed.js"
                joinGridValue_js: str = "node_modules/postcss-ordered-values/src/lib/joinGridValue.js"
            lib = _node_modules_postcss_ordered_values_src_lib()

            class _node_modules_postcss_ordered_values_src_rules:
                listStyle_js: str = "node_modules/postcss-ordered-values/src/rules/listStyle.js"
                animation_js: str = "node_modules/postcss-ordered-values/src/rules/animation.js"
                boxShadow_js: str = "node_modules/postcss-ordered-values/src/rules/boxShadow.js"
                grid_js: str = "node_modules/postcss-ordered-values/src/rules/grid.js"
                columns_js: str = "node_modules/postcss-ordered-values/src/rules/columns.js"
                border_js: str = "node_modules/postcss-ordered-values/src/rules/border.js"
                flexFlow_js: str = "node_modules/postcss-ordered-values/src/rules/flexFlow.js"
                transition_js: str = "node_modules/postcss-ordered-values/src/rules/transition.js"
            rules = _node_modules_postcss_ordered_values_src_rules()
        src = _node_modules_postcss_ordered_values_src()
    postcss_ordered_values = _node_modules_postcss_ordered_values()

    class _node_modules_cssnano_utils:

        class _node_modules_cssnano_utils_src:
            sameParent_js: str = "node_modules/cssnano-utils/src/sameParent.js"
            rawCache_js: str = "node_modules/cssnano-utils/src/rawCache.js"
            index_js: str = "node_modules/cssnano-utils/src/index.js"
            getArguments_js: str = "node_modules/cssnano-utils/src/getArguments.js"
        src = _node_modules_cssnano_utils_src()
    cssnano_utils = _node_modules_cssnano_utils()
    pify: str = "node_modules/pify/index.js"
    has_flag: str = "node_modules/has-flag/index.js"

    class _node_modules_postcss_modules_extract_imports:

        class _node_modules_postcss_modules_extract_imports_src:
            topologicalSort_js: str = "node_modules/postcss-modules-extract-imports/src/topologicalSort.js"
            index_js: str = "node_modules/postcss-modules-extract-imports/src/index.js"
        src = _node_modules_postcss_modules_extract_imports_src()
    postcss_modules_extract_imports = _node_modules_postcss_modules_extract_imports()

    class _node_modules_source_map_support:
        register_js: str = "node_modules/source-map-support/register.js"
        register_hook_require_js: str = "node_modules/source-map-support/register-hook-require.js"
        source_map_support_js: str = "node_modules/source-map-support/source-map-support.js"
        browser_source_map_support_js: str = "node_modules/source-map-support/browser-source-map-support.js"
    source_map_support = _node_modules_source_map_support()
    is_glob: str = "node_modules/is-glob/index.js"
    lodash_camelcase: str = "node_modules/lodash.camelcase/index.js"

    class _node_modules_terser:
        main_js: str = "node_modules/terser/main.js"

        class _node_modules_terser_node_modules:

            class _node_modules_terser_node_modules_commander:
                index_js: str = "node_modules/terser/node_modules/commander/index.js"
            commander = _node_modules_terser_node_modules_commander()
        node_modules = _node_modules_terser_node_modules()

        class _node_modules_terser_lib:
            parse_js: str = "node_modules/terser/lib/parse.js"
            sourcemap_js: str = "node_modules/terser/lib/sourcemap.js"
            equivalent_to_js: str = "node_modules/terser/lib/equivalent-to.js"
            size_js: str = "node_modules/terser/lib/size.js"
            cli_js: str = "node_modules/terser/lib/cli.js"
            output_js: str = "node_modules/terser/lib/output.js"
            minify_js: str = "node_modules/terser/lib/minify.js"
            transform_js: str = "node_modules/terser/lib/transform.js"
            propmangle_js: str = "node_modules/terser/lib/propmangle.js"
            mozilla_ast_js: str = "node_modules/terser/lib/mozilla-ast.js"
            ast_js: str = "node_modules/terser/lib/ast.js"
            scope_js: str = "node_modules/terser/lib/scope.js"

            class _node_modules_terser_lib_utils:
                index_js: str = "node_modules/terser/lib/utils/index.js"
                first_in_statement_js: str = "node_modules/terser/lib/utils/first_in_statement.js"
            utils = _node_modules_terser_lib_utils()

            class _node_modules_terser_lib_compress:
                reduce_vars_js: str = "node_modules/terser/lib/compress/reduce-vars.js"
                evaluate_js: str = "node_modules/terser/lib/compress/evaluate.js"
                drop_unused_js: str = "node_modules/terser/lib/compress/drop-unused.js"
                common_js: str = "node_modules/terser/lib/compress/common.js"
                index_js: str = "node_modules/terser/lib/compress/index.js"
                native_objects_js: str = "node_modules/terser/lib/compress/native-objects.js"
                drop_side_effect_free_js: str = "node_modules/terser/lib/compress/drop-side-effect-free.js"
                tighten_body_js: str = "node_modules/terser/lib/compress/tighten-body.js"
                compressor_flags_js: str = "node_modules/terser/lib/compress/compressor-flags.js"
                global_defs_js: str = "node_modules/terser/lib/compress/global-defs.js"
                inline_js: str = "node_modules/terser/lib/compress/inline.js"
                inference_js: str = "node_modules/terser/lib/compress/inference.js"
            compress = _node_modules_terser_lib_compress()
        lib = _node_modules_terser_lib()
        dist: str = "node_modules/terser/dist/bundle.min.js"

        class _node_modules_terser_tools:
            domprops_js: str = "node_modules/terser/tools/domprops.js"
            props_html: str = "node_modules/terser/tools/props.html"
        tools = _node_modules_terser_tools()
    terser = _node_modules_terser()

    class _node_modules_postcss:

        class _node_modules_postcss_lib:
            postcss_js: str = "node_modules/postcss/lib/postcss.js"
            comment_js: str = "node_modules/postcss/lib/comment.js"
            parse_js: str = "node_modules/postcss/lib/parse.js"
            at_rule_js: str = "node_modules/postcss/lib/at-rule.js"
            no_work_result_js: str = "node_modules/postcss/lib/no-work-result.js"
            declaration_js: str = "node_modules/postcss/lib/declaration.js"
            list_js: str = "node_modules/postcss/lib/list.js"
            fromJSON_js: str = "node_modules/postcss/lib/fromJSON.js"
            lazy_result_js: str = "node_modules/postcss/lib/lazy-result.js"
            rule_js: str = "node_modules/postcss/lib/rule.js"
            warning_js: str = "node_modules/postcss/lib/warning.js"
            parser_js: str = "node_modules/postcss/lib/parser.js"
            tokenize_js: str = "node_modules/postcss/lib/tokenize.js"
            stringify_js: str = "node_modules/postcss/lib/stringify.js"
            node_js: str = "node_modules/postcss/lib/node.js"
            root_js: str = "node_modules/postcss/lib/root.js"
            previous_map_js: str = "node_modules/postcss/lib/previous-map.js"
            container_js: str = "node_modules/postcss/lib/container.js"
            processor_js: str = "node_modules/postcss/lib/processor.js"
            symbols_js: str = "node_modules/postcss/lib/symbols.js"
            terminal_highlight_js: str = "node_modules/postcss/lib/terminal-highlight.js"
            result_js: str = "node_modules/postcss/lib/result.js"
            input_js: str = "node_modules/postcss/lib/input.js"
            stringifier_js: str = "node_modules/postcss/lib/stringifier.js"
            css_syntax_error_js: str = "node_modules/postcss/lib/css-syntax-error.js"
            map_generator_js: str = "node_modules/postcss/lib/map-generator.js"
            document_js: str = "node_modules/postcss/lib/document.js"
            warn_once_js: str = "node_modules/postcss/lib/warn-once.js"
        lib = _node_modules_postcss_lib()
    postcss = _node_modules_postcss()

    class _node_modules_lines_and_columns:
        build: str = "node_modules/lines-and-columns/build/index.js"
    lines_and_columns = _node_modules_lines_and_columns()

    class _node_modules_postcss_minify_selectors:

        class _node_modules_postcss_minify_selectors_src:
            index_js: str = "node_modules/postcss-minify-selectors/src/index.js"
            lib: str = "node_modules/postcss-minify-selectors/src/lib/canUnquote.js"
        src = _node_modules_postcss_minify_selectors_src()
    postcss_minify_selectors = _node_modules_postcss_minify_selectors()
    import_cwd: str = "node_modules/import-cwd/index.js"
    shebang_command: str = "node_modules/shebang-command/index.js"

    class _node_modules_wrap_ansi_cjs:
        index_js: str = "node_modules/wrap-ansi-cjs/index.js"

        class _node_modules_wrap_ansi_cjs_node_modules:
            strip_ansi: str = "node_modules/wrap-ansi-cjs/node_modules/strip-ansi/index.js"
            ansi_regex: str = "node_modules/wrap-ansi-cjs/node_modules/ansi-regex/index.js"
            string_width: str = "node_modules/wrap-ansi-cjs/node_modules/string-width/index.js"

            class _node_modules_wrap_ansi_cjs_node_modules_emoji_regex:
                text_js: str = "node_modules/wrap-ansi-cjs/node_modules/emoji-regex/text.js"
                index_js: str = "node_modules/wrap-ansi-cjs/node_modules/emoji-regex/index.js"

                class _node_modules_wrap_ansi_cjs_node_modules_emoji_regex_es2015:
                    text_js: str = "node_modules/wrap-ansi-cjs/node_modules/emoji-regex/es2015/text.js"
                    index_js: str = "node_modules/wrap-ansi-cjs/node_modules/emoji-regex/es2015/index.js"
                es2015 = _node_modules_wrap_ansi_cjs_node_modules_emoji_regex_es2015()
            emoji_regex = _node_modules_wrap_ansi_cjs_node_modules_emoji_regex()
        node_modules = _node_modules_wrap_ansi_cjs_node_modules()
    wrap_ansi_cjs = _node_modules_wrap_ansi_cjs()

    class _node_modules_postcss_calc:

        class _node_modules_postcss_calc_src:
            parser_js: str = "node_modules/postcss-calc/src/parser.js"
            index_js: str = "node_modules/postcss-calc/src/index.js"

            class _node_modules_postcss_calc_src_lib:
                convertUnit_js: str = "node_modules/postcss-calc/src/lib/convertUnit.js"
                transform_js: str = "node_modules/postcss-calc/src/lib/transform.js"
                reducer_js: str = "node_modules/postcss-calc/src/lib/reducer.js"
                stringifier_js: str = "node_modules/postcss-calc/src/lib/stringifier.js"
            lib = _node_modules_postcss_calc_src_lib()

            class _node_modules_postcss_calc_src_tests:
                convertUnit_js: str = "node_modules/postcss-calc/src/__tests__/convertUnit.js"
                index_js: str = "node_modules/postcss-calc/src/__tests__/index.js"
            tests = _node_modules_postcss_calc_src_tests()
        src = _node_modules_postcss_calc_src()
    postcss_calc = _node_modules_postcss_calc()
    to_regex_range: str = "node_modules/to-regex-range/index.js"

    class _node_modules_postcss_normalize_timing_functions:
        src: str = "node_modules/postcss-normalize-timing-functions/src/index.js"
    postcss_normalize_timing_functions = _node_modules_postcss_normalize_timing_functions()

    class _node_modules_p_queue:

        class _node_modules_p_queue_dist:
            priority_queue_js: str = "node_modules/p-queue/dist/priority-queue.js"
            index_js: str = "node_modules/p-queue/dist/index.js"
            options_js: str = "node_modules/p-queue/dist/options.js"
            lower_bound_js: str = "node_modules/p-queue/dist/lower-bound.js"
            queue_js: str = "node_modules/p-queue/dist/queue.js"
        dist = _node_modules_p_queue_dist()
    p_queue = _node_modules_p_queue()

    class _node_modules_postcss_minify_gradients:

        class _node_modules_postcss_minify_gradients_src:
            index_js: str = "node_modules/postcss-minify-gradients/src/index.js"
            isColorStop_js: str = "node_modules/postcss-minify-gradients/src/isColorStop.js"
        src = _node_modules_postcss_minify_gradients_src()
    postcss_minify_gradients = _node_modules_postcss_minify_gradients()

    class _node_modules_rollup:

        class _node_modules_rollup_plugin_terser:

            class _node_modules_rollup_plugin_terser_dist:
                cjs: str = "node_modules/@rollup/plugin-terser/dist/cjs/index.js"
                es: str = "node_modules/@rollup/plugin-terser/dist/es/index.js"
            dist = _node_modules_rollup_plugin_terser_dist()
        plugin_terser = _node_modules_rollup_plugin_terser()

        class _node_modules_rollup_plugin_node_resolve:

            class _node_modules_rollup_plugin_node_resolve_dist:
                cjs: str = "node_modules/@rollup/plugin-node-resolve/dist/cjs/index.js"
                es: str = "node_modules/@rollup/plugin-node-resolve/dist/es/index.js"
            dist = _node_modules_rollup_plugin_node_resolve_dist()
        plugin_node_resolve = _node_modules_rollup_plugin_node_resolve()

        class _node_modules_rollup_pluginutils:

            class _node_modules_rollup_pluginutils_dist:
                cjs: str = "node_modules/@rollup/pluginutils/dist/cjs/index.js"
                es: str = "node_modules/@rollup/pluginutils/dist/es/index.js"
            dist = _node_modules_rollup_pluginutils_dist()
        pluginutils = _node_modules_rollup_pluginutils()

        class _node_modules_rollup_plugin_commonjs:

            class _node_modules_rollup_plugin_commonjs_dist:
                cjs: str = "node_modules/@rollup/plugin-commonjs/dist/cjs/index.js"
                es: str = "node_modules/@rollup/plugin-commonjs/dist/es/index.js"
            dist = _node_modules_rollup_plugin_commonjs_dist()
        plugin_commonjs = _node_modules_rollup_plugin_commonjs()
    rollup = _node_modules_rollup()
    postcss_nested: str = "node_modules/postcss-nested/index.js"

    class _node_modules_package_json_from_dist:

        class _node_modules_package_json_from_dist_dist:
            esm: str = "node_modules/package-json-from-dist/dist/esm/index.js"
            commonjs: str = "node_modules/package-json-from-dist/dist/commonjs/index.js"
        dist = _node_modules_package_json_from_dist_dist()
    package_json_from_dist = _node_modules_package_json_from_dist()
    resolve_from: str = "node_modules/resolve-from/index.js"

    class _node_modules_mz:
        fs_js: str = "node_modules/mz/fs.js"
        zlib_js: str = "node_modules/mz/zlib.js"
        index_js: str = "node_modules/mz/index.js"
        crypto_js: str = "node_modules/mz/crypto.js"
        child_process_js: str = "node_modules/mz/child_process.js"
        dns_js: str = "node_modules/mz/dns.js"
        readline_js: str = "node_modules/mz/readline.js"
    mz = _node_modules_mz()

    class _node_modules_cross_spawn:
        index_js: str = "node_modules/cross-spawn/index.js"

        class _node_modules_cross_spawn_lib:
            parse_js: str = "node_modules/cross-spawn/lib/parse.js"
            enoent_js: str = "node_modules/cross-spawn/lib/enoent.js"

            class _node_modules_cross_spawn_lib_util:
                resolveCommand_js: str = "node_modules/cross-spawn/lib/util/resolveCommand.js"
                readShebang_js: str = "node_modules/cross-spawn/lib/util/readShebang.js"
                escape_js: str = "node_modules/cross-spawn/lib/util/escape.js"
            util = _node_modules_cross_spawn_lib_util()
        lib = _node_modules_cross_spawn_lib()
    cross_spawn = _node_modules_cross_spawn()

    class _node_modules_postcss_convert_values:

        class _node_modules_postcss_convert_values_src:
            index_js: str = "node_modules/postcss-convert-values/src/index.js"
            lib: str = "node_modules/postcss-convert-values/src/lib/convert.js"
        src = _node_modules_postcss_convert_values_src()
    postcss_convert_values = _node_modules_postcss_convert_values()

    class _node_modules_postcss_discard_overridden:
        src: str = "node_modules/postcss-discard-overridden/src/index.js"
    postcss_discard_overridden = _node_modules_postcss_discard_overridden()

    class _node_modules_fast_glob:

        class _node_modules_fast_glob_node_modules:
            glob_parent: str = "node_modules/fast-glob/node_modules/glob-parent/index.js"
        node_modules = _node_modules_fast_glob_node_modules()

        class _node_modules_fast_glob_out:
            settings_js: str = "node_modules/fast-glob/out/settings.js"
            index_js: str = "node_modules/fast-glob/out/index.js"

            class _node_modules_fast_glob_out_utils:
                fs_js: str = "node_modules/fast-glob/out/utils/fs.js"
                string_js: str = "node_modules/fast-glob/out/utils/string.js"
                array_js: str = "node_modules/fast-glob/out/utils/array.js"
                errno_js: str = "node_modules/fast-glob/out/utils/errno.js"
                index_js: str = "node_modules/fast-glob/out/utils/index.js"
                path_js: str = "node_modules/fast-glob/out/utils/path.js"
                stream_js: str = "node_modules/fast-glob/out/utils/stream.js"
                pattern_js: str = "node_modules/fast-glob/out/utils/pattern.js"
            utils = _node_modules_fast_glob_out_utils()

            class _node_modules_fast_glob_out_readers:
                async_js: str = "node_modules/fast-glob/out/readers/async.js"
                reader_js: str = "node_modules/fast-glob/out/readers/reader.js"
                stream_js: str = "node_modules/fast-glob/out/readers/stream.js"
                sync_js: str = "node_modules/fast-glob/out/readers/sync.js"
            readers = _node_modules_fast_glob_out_readers()
            managers: str = "node_modules/fast-glob/out/managers/tasks.js"

            class _node_modules_fast_glob_out_providers:
                async_js: str = "node_modules/fast-glob/out/providers/async.js"
                provider_js: str = "node_modules/fast-glob/out/providers/provider.js"
                stream_js: str = "node_modules/fast-glob/out/providers/stream.js"
                sync_js: str = "node_modules/fast-glob/out/providers/sync.js"

                class _node_modules_fast_glob_out_providers_filters:
                    entry_js: str = "node_modules/fast-glob/out/providers/filters/entry.js"
                    error_js: str = "node_modules/fast-glob/out/providers/filters/error.js"
                    deep_js: str = "node_modules/fast-glob/out/providers/filters/deep.js"
                filters = _node_modules_fast_glob_out_providers_filters()

                class _node_modules_fast_glob_out_providers_matchers:
                    matcher_js: str = "node_modules/fast-glob/out/providers/matchers/matcher.js"
                    partial_js: str = "node_modules/fast-glob/out/providers/matchers/partial.js"
                matchers = _node_modules_fast_glob_out_providers_matchers()
                transformers: str = "node_modules/fast-glob/out/providers/transformers/entry.js"
            providers = _node_modules_fast_glob_out_providers()
            types: str = "node_modules/fast-glob/out/types/index.js"
        out = _node_modules_fast_glob_out()
    fast_glob = _node_modules_fast_glob()
    normalize_url: str = "node_modules/normalize-url/index.js"

    class _node_modules_picomatch:
        index_js: str = "node_modules/picomatch/index.js"

        class _node_modules_picomatch_lib:
            constants_js: str = "node_modules/picomatch/lib/constants.js"
            parse_js: str = "node_modules/picomatch/lib/parse.js"
            utils_js: str = "node_modules/picomatch/lib/utils.js"
            picomatch_js: str = "node_modules/picomatch/lib/picomatch.js"
            scan_js: str = "node_modules/picomatch/lib/scan.js"
        lib = _node_modules_picomatch_lib()
    picomatch = _node_modules_picomatch()

    class _node_modules_trysound:

        class _node_modules_trysound_sax:
            lib: str = "node_modules/@trysound/sax/lib/sax.js"
        sax = _node_modules_trysound_sax()
    trysound = _node_modules_trysound()
    anymatch: str = "node_modules/anymatch/index.js"
    merge2: str = "node_modules/merge2/index.js"

    class _node_modules_emoji_regex:
        text_js: str = "node_modules/emoji-regex/text.js"
        RGI_Emoji_js: str = "node_modules/emoji-regex/RGI_Emoji.js"
        index_js: str = "node_modules/emoji-regex/index.js"

        class _node_modules_emoji_regex_es2015:
            text_js: str = "node_modules/emoji-regex/es2015/text.js"
            RGI_Emoji_js: str = "node_modules/emoji-regex/es2015/RGI_Emoji.js"
            index_js: str = "node_modules/emoji-regex/es2015/index.js"
        es2015 = _node_modules_emoji_regex_es2015()
    emoji_regex = _node_modules_emoji_regex()


class Bundle:
    tailwind_config_js: str = "./tailwind.config.js"
    input_css: str = "./input.css"
    rollup_config_js: str = "./rollup.config.js"
    node_modules=_node_modules()
    dist: str = "dist/output.css"


js_bundle = Bundle()