# AUTOGENERATED DON'T EDIT
# Please make changes to the code generator             (distutils/ccompiler_opt.py)
hash = 455466792
data = \
{'cache_infile': True,
 'cache_me': {"('cc_test_flags', ['/O2'])": True,
              "('cc_test_flags', ['/WX'])": True,
              "('feature_flags', 'SSE')": [],
              "('feature_flags', 'SSE2')": [],
              "('feature_flags', set())": [],
              "('feature_is_supported', 'AVX', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'AVX2', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'AVX512CD', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'AVX512F', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'AVX512_CLX', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'AVX512_CNL', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'AVX512_ICL', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'AVX512_SKX', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'F16C', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'FMA3', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'POPCNT', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'SSE', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'SSE2', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'SSE3', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'SSE41', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'SSE42', 'force_flags', 'macros', None, [])": False,
              "('feature_is_supported', 'SSSE3', 'force_flags', 'macros', None, [])": False,
              "('feature_test', 'SSE', None, 'macros', [])": False,
              "('feature_test', 'SSE2', None, 'macros', [])": False},
 'cache_private': {'sources_status'},
 'cc_flags': {'native': [], 'opt': ['/O2'], 'werror': ['/WX']},
 'cc_has_debug': False,
 'cc_has_native': False,
 'cc_is_cached': True,
 'cc_is_clang': False,
 'cc_is_gcc': False,
 'cc_is_icc': False,
 'cc_is_iccw': False,
 'cc_is_msvc': True,
 'cc_is_nocc': False,
 'cc_march': 'x64',
 'cc_name': 'msvc',
 'cc_noopt': False,
 'cc_on_aarch64': False,
 'cc_on_armhf': False,
 'cc_on_noarch': False,
 'cc_on_ppc64': False,
 'cc_on_ppc64le': False,
 'cc_on_s390x': False,
 'cc_on_x64': True,
 'cc_on_x86': False,
 'feature_is_cached': True,
 'feature_min': {'SSE2', 'SSE', 'SSE3'},
 'feature_supported': {'AVX': {'flags': ['/arch:AVX'],
                               'headers': ['immintrin.h'],
                               'implies': ['SSE42'],
                               'implies_detect': False,
                               'interest': 8},
                       'AVX2': {'flags': ['/arch:AVX2'],
                                'implies': ['F16C', 'FMA3'],
                                'interest': 13},
                       'AVX512CD': {'flags': ['/arch:AVX512'],
                                    'implies': ['AVX512F', 'AVX512_SKX'],
                                    'interest': 21},
                       'AVX512F': {'extra_checks': ['AVX512F_REDUCE'],
                                   'flags': ['/arch:AVX512'],
                                   'implies': ['AVX2', 'AVX512CD',
                                               'AVX512_SKX'],
                                   'implies_detect': False,
                                   'interest': 20},
                       'AVX512_CLX': {'detect': ['AVX512_CLX'],
                                      'group': ['AVX512VNNI'],
                                      'implies': ['AVX512_SKX'],
                                      'interest': 43},
                       'AVX512_CNL': {'detect': ['AVX512_CNL'],
                                      'group': ['AVX512IFMA', 'AVX512VBMI'],
                                      'implies': ['AVX512_SKX'],
                                      'implies_detect': False,
                                      'interest': 44},
                       'AVX512_ICL': {'detect': ['AVX512_ICL'],
                                      'group': ['AVX512VBMI2', 'AVX512BITALG',
                                                'AVX512VPOPCNTDQ'],
                                      'implies': ['AVX512_CLX', 'AVX512_CNL'],
                                      'implies_detect': False,
                                      'interest': 45},
                       'AVX512_SKX': {'detect': ['AVX512_SKX'],
                                      'extra_checks': ['AVX512BW_MASK',
                                                       'AVX512DQ_MASK'],
                                      'flags': ['/arch:AVX512'],
                                      'group': ['AVX512VL', 'AVX512BW',
                                                'AVX512DQ'],
                                      'implies': ['AVX512CD'],
                                      'implies_detect': False,
                                      'interest': 42},
                       'F16C': {'implies': ['AVX'], 'interest': 11},
                       'FMA3': {'flags': ['/arch:AVX2'],
                                'implies': ['F16C', 'AVX2'],
                                'interest': 12},
                       'FMA4': {'headers': ['ammintrin.h'],
                                'implies': ['AVX'],
                                'interest': 10},
                       'POPCNT': {'headers': ['nmmintrin.h'],
                                  'implies': ['SSE41'],
                                  'interest': 6},
                       'SSE': {'headers': ['xmmintrin.h'],
                               'implies': ['SSE2'],
                               'interest': 1},
                       'SSE2': {'headers': ['emmintrin.h'],
                                'implies': ['SSE'],
                                'interest': 2},
                       'SSE3': {'headers': ['pmmintrin.h'],
                                'implies': ['SSE2'],
                                'interest': 3},
                       'SSE41': {'headers': ['smmintrin.h'],
                                 'implies': ['SSSE3'],
                                 'interest': 5},
                       'SSE42': {'implies': ['POPCNT'], 'interest': 7},
                       'SSSE3': {'headers': ['tmmintrin.h'],
                                 'implies': ['SSE3'],
                                 'interest': 4},
                       'XOP': {'headers': ['ammintrin.h'],
                               'implies': ['AVX'],
                               'interest': 9}},
 'hit_cache': False,
 'parse_baseline_flags': [],
 'parse_baseline_names': [],
 'parse_dispatch_names': [],
 'parse_is_cached': True,
 'parse_target_groups': {'SIMD_TEST': (True, [], [])},
 'sources_status': {}}