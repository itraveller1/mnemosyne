# -*- mode: python -*-

import os, sys, shutil

block_cipher = None

datas = [('mo', 'mo'), ('pixmaps', 'pixmaps')]
excludes = ['PyQt5', 'tcl', 'tk']
binaries = []

hiddenimports = [
             'argon2-cffi',
             'PyQt6.sip',
             'google',
             'google.cloud',
             'google.api'
             'google.api.core',
             'mnemosyne.version',
             'mnemosyne.libmnemosyne.card',
             'mnemosyne.libmnemosyne.card_type',
             'mnemosyne.libmnemosyne.card_type_converter',
             'mnemosyne.libmnemosyne.component',
             'mnemosyne.libmnemosyne.component_manager',
             'mnemosyne.libmnemosyne.configuration',
             'mnemosyne.libmnemosyne.controller',
             'mnemosyne.libmnemosyne.criterion',
             'mnemosyne.libmnemosyne.database',
             'mnemosyne.libmnemosyne.fact',
             'mnemosyne.libmnemosyne.fact_view',
             'mnemosyne.libmnemosyne.file_format',
             'mnemosyne.libmnemosyne.filter',
             'mnemosyne.libmnemosyne.gui_translator',
             'mnemosyne.libmnemosyne.hook',
             'mnemosyne.libmnemosyne.language',
             'mnemosyne.libmnemosyne.logger',
             'mnemosyne.libmnemosyne.log_uploader',
             'mnemosyne.libmnemosyne.plugin',
             'mnemosyne.libmnemosyne.pronouncer',
             'mnemosyne.libmnemosyne.renderer',
             'mnemosyne.libmnemosyne.render_chain',
             'mnemosyne.libmnemosyne.review_controller',
             'mnemosyne.libmnemosyne.scheduler',
             'mnemosyne.libmnemosyne.statistics_page',
             'mnemosyne.libmnemosyne.stopwatch',
             'mnemosyne.libmnemosyne.study_mode',
             'mnemosyne.libmnemosyne.sync_server',
             'mnemosyne.libmnemosyne.tag',
             'mnemosyne.libmnemosyne.tag_tree',
             'mnemosyne.libmnemosyne.translator',
             'mnemosyne.libmnemosyne.ui_component',
             'mnemosyne.libmnemosyne.utils',
             'mnemosyne.libmnemosyne.card_types.both_ways',
             'mnemosyne.libmnemosyne.card_types.cloze',
             'mnemosyne.libmnemosyne.card_types.front_to_back',
             'mnemosyne.libmnemosyne.card_types.map',
             'mnemosyne.libmnemosyne.card_types.M_sided',
             'mnemosyne.libmnemosyne.card_types.sentence',
             'mnemosyne.libmnemosyne.card_types.vocabulary',
             'mnemosyne.libmnemosyne.controllers.default_controller',
             'mnemosyne.libmnemosyne.criteria.default_criterion',
             'mnemosyne.libmnemosyne.databases.SQLite',
             'mnemosyne.libmnemosyne.databases.SQLite_criterion_applier',
             'mnemosyne.libmnemosyne.databases.SQLite_logging',
             'mnemosyne.libmnemosyne.databases.SQLite_media',
             'mnemosyne.libmnemosyne.databases.SQLite_no_pregenerated_data',
             'mnemosyne.libmnemosyne.databases.SQLite_statistics',
             'mnemosyne.libmnemosyne.databases.SQLite_sync',
             'mnemosyne.libmnemosyne.databases._apsw',
             'mnemosyne.libmnemosyne.databases._sqlite3',
             'mnemosyne.libmnemosyne.file_formats.anki2',
             'mnemosyne.libmnemosyne.file_formats.cuecard_wcu',
             'mnemosyne.libmnemosyne.file_formats.media_preprocessor',
             'mnemosyne.libmnemosyne.file_formats.mnemosyne1',
             'mnemosyne.libmnemosyne.file_formats.mnemosyne1_mem',
             'mnemosyne.libmnemosyne.file_formats.mnemosyne1_xml',
             'mnemosyne.libmnemosyne.file_formats.mnemosyne2_cards',
             'mnemosyne.libmnemosyne.file_formats.mnemosyne2_db',
             'mnemosyne.libmnemosyne.file_formats.science_log_parser',
             'mnemosyne.libmnemosyne.file_formats.smconv_XML',
             'mnemosyne.libmnemosyne.file_formats.supermemo_7_txt',
             'mnemosyne.libmnemosyne.file_formats.tsv',
             'mnemosyne.libmnemosyne.filters.escape_to_html',
             'mnemosyne.libmnemosyne.filters.escape_to_html_for_card_browser',
             'mnemosyne.libmnemosyne.filters.expand_paths',
             'mnemosyne.libmnemosyne.filters.html5_audio',
             'mnemosyne.libmnemosyne.filters.html5_video',
             'mnemosyne.libmnemosyne.filters.latex',
             'mnemosyne.libmnemosyne.filters.non_latin_font_size_increase',
             'mnemosyne.libmnemosyne.filters.RTL_handler',
             'mnemosyne.libmnemosyne.gui_translators.gettext_gui_translator',
             'mnemosyne.libmnemosyne.gui_translators.no_gui_translator',
             'mnemosyne.libmnemosyne.languages.afrikaans',
             'mnemosyne.libmnemosyne.languages.albanian',
             'mnemosyne.libmnemosyne.languages.amharic',
             'mnemosyne.libmnemosyne.languages.arabic',
             'mnemosyne.libmnemosyne.languages.armenian',
             'mnemosyne.libmnemosyne.languages.azerbaijani',
             'mnemosyne.libmnemosyne.languages.basque',
             'mnemosyne.libmnemosyne.languages.belarusian',
             'mnemosyne.libmnemosyne.languages.bengali',
             'mnemosyne.libmnemosyne.languages.bosnian',
             'mnemosyne.libmnemosyne.languages.bulgarian',
             'mnemosyne.libmnemosyne.languages.catalan',
             'mnemosyne.libmnemosyne.languages.cebuano',
             'mnemosyne.libmnemosyne.languages.chinese',
             'mnemosyne.libmnemosyne.languages.corsican',
             'mnemosyne.libmnemosyne.languages.croatian',
             'mnemosyne.libmnemosyne.languages.czech',
             'mnemosyne.libmnemosyne.languages.danish',
             'mnemosyne.libmnemosyne.languages.dutch',
             'mnemosyne.libmnemosyne.languages.english',
             'mnemosyne.libmnemosyne.languages.esperanto',
             'mnemosyne.libmnemosyne.languages.estonian',
             'mnemosyne.libmnemosyne.languages.finnish',
             'mnemosyne.libmnemosyne.languages.french',
             'mnemosyne.libmnemosyne.languages.frisian',
             'mnemosyne.libmnemosyne.languages.gaelic',
             'mnemosyne.libmnemosyne.languages.galician',
             'mnemosyne.libmnemosyne.languages.georgian',
             'mnemosyne.libmnemosyne.languages.german',
             'mnemosyne.libmnemosyne.languages.greek',
             'mnemosyne.libmnemosyne.languages.gujarati',
             'mnemosyne.libmnemosyne.languages.haitian',
             'mnemosyne.libmnemosyne.languages.hausa',
             'mnemosyne.libmnemosyne.languages.hawaiian',
             'mnemosyne.libmnemosyne.languages.hebrew',
             'mnemosyne.libmnemosyne.languages.hindi',
             'mnemosyne.libmnemosyne.languages.hmong',
             'mnemosyne.libmnemosyne.languages.hungarian',
             'mnemosyne.libmnemosyne.languages.icelandic',
             'mnemosyne.libmnemosyne.languages.igbo',
             'mnemosyne.libmnemosyne.languages.indonesian',
             'mnemosyne.libmnemosyne.languages.irish',
             'mnemosyne.libmnemosyne.languages.italian',
             'mnemosyne.libmnemosyne.languages.japanese',
             'mnemosyne.libmnemosyne.languages.javanese',
             'mnemosyne.libmnemosyne.languages.kannada',
             'mnemosyne.libmnemosyne.languages.kazakh',
             'mnemosyne.libmnemosyne.languages.khmer',
             'mnemosyne.libmnemosyne.languages.korean',
             'mnemosyne.libmnemosyne.languages.kurdish',
             'mnemosyne.libmnemosyne.languages.kyrgyz',
             'mnemosyne.libmnemosyne.languages.lao',
             'mnemosyne.libmnemosyne.languages.latin',
             'mnemosyne.libmnemosyne.languages.latvian',
             'mnemosyne.libmnemosyne.languages.lithuanian',
             'mnemosyne.libmnemosyne.languages.luxembourgish',
             'mnemosyne.libmnemosyne.languages.macedonian',
             'mnemosyne.libmnemosyne.languages.malagasy',
             'mnemosyne.libmnemosyne.languages.malay',
             'mnemosyne.libmnemosyne.languages.malayalam',
             'mnemosyne.libmnemosyne.languages.maltese',
             'mnemosyne.libmnemosyne.languages.maori',
             'mnemosyne.libmnemosyne.languages.marathi',
             'mnemosyne.libmnemosyne.languages.mongolian',
             'mnemosyne.libmnemosyne.languages.myanmar',
             'mnemosyne.libmnemosyne.languages.nepali',
             'mnemosyne.libmnemosyne.languages.norwegian',
             'mnemosyne.libmnemosyne.languages.nyanja',
             'mnemosyne.libmnemosyne.languages.pashto',
             'mnemosyne.libmnemosyne.languages.persian',
             'mnemosyne.libmnemosyne.languages.polish',
             'mnemosyne.libmnemosyne.languages.portuguese',
             'mnemosyne.libmnemosyne.languages.punjabi',
             'mnemosyne.libmnemosyne.languages.romanian',
             'mnemosyne.libmnemosyne.languages.russian',
             'mnemosyne.libmnemosyne.languages.samoan',
             'mnemosyne.libmnemosyne.languages.serbian',
             'mnemosyne.libmnemosyne.languages.sesotho',
             'mnemosyne.libmnemosyne.languages.shona',
             'mnemosyne.libmnemosyne.languages.sindhi',
             'mnemosyne.libmnemosyne.languages.sinhala',
             'mnemosyne.libmnemosyne.languages.slovak',
             'mnemosyne.libmnemosyne.languages.slovenian',
             'mnemosyne.libmnemosyne.languages.somali',
             'mnemosyne.libmnemosyne.languages.spanish',
             'mnemosyne.libmnemosyne.languages.sundanese',
             'mnemosyne.libmnemosyne.languages.swahili',
             'mnemosyne.libmnemosyne.languages.swedish',
             'mnemosyne.libmnemosyne.languages.tagalog',
             'mnemosyne.libmnemosyne.languages.tajik',
             'mnemosyne.libmnemosyne.languages.tamil',
             'mnemosyne.libmnemosyne.languages.telugu',
             'mnemosyne.libmnemosyne.languages.thai',
             'mnemosyne.libmnemosyne.languages.turkish',
             'mnemosyne.libmnemosyne.languages.ukrainian',
             'mnemosyne.libmnemosyne.languages.urdu',
             'mnemosyne.libmnemosyne.languages.uzbek',
             'mnemosyne.libmnemosyne.languages.vietnamese',
             'mnemosyne.libmnemosyne.languages.welsh',
             'mnemosyne.libmnemosyne.languages.xhosa',
             'mnemosyne.libmnemosyne.languages.yiddish',
             'mnemosyne.libmnemosyne.languages.yoruba',
             'mnemosyne.libmnemosyne.languages.zulu',
             'mnemosyne.libmnemosyne.languages.arabic',
             'mnemosyne.libmnemosyne.languages.english',
             'mnemosyne.libmnemosyne.languages.french',
             'mnemosyne.libmnemosyne.loggers.database_logger',
             'mnemosyne.libmnemosyne.pronouncer',
             'mnemosyne.libmnemosyne.pronouncers.google_pronouncer',
             'mnemosyne.libmnemosyne.renderers.html_css',
             'mnemosyne.libmnemosyne.renderers.html_css_card_browser',
             'mnemosyne.libmnemosyne.renderers.plain_text',
             'mnemosyne.libmnemosyne.renderers.anki_renderer',
             'mnemosyne.libmnemosyne.renderers.anki.decorator',
             'mnemosyne.libmnemosyne.renderers.anki.hooks',
             'mnemosyne.libmnemosyne.renderers.anki.lang',
             'mnemosyne.libmnemosyne.renderers.anki.utils',
             'mnemosyne.libmnemosyne.renderers.anki.template',
             'mnemosyne.libmnemosyne.renderers.anki.template.furigana',
             'mnemosyne.libmnemosyne.renderers.anki.template.hint',
             'mnemosyne.libmnemosyne.renderers.anki.template.template',
             'mnemosyne.libmnemosyne.renderers.anki.template.view',
             'mnemosyne.libmnemosyne.render_chains.card_browser_render_chain',
             'mnemosyne.libmnemosyne.render_chains.default_render_chain',
             'mnemosyne.libmnemosyne.render_chains.plain_text_chain',
             'mnemosyne.libmnemosyne.render_chains.sync_to_card_only_client',
             'mnemosyne.libmnemosyne.review_controllers.SM2_controller',
             'mnemosyne.libmnemosyne.review_controllers.SM2_controller_cramming',
             'mnemosyne.libmnemosyne.schedulers.cramming',
             'mnemosyne.libmnemosyne.schedulers.SM2_mnemosyne',
             'mnemosyne.libmnemosyne.statistics_pages.cards_added',
             'mnemosyne.libmnemosyne.statistics_pages.cards_learned',
             'mnemosyne.libmnemosyne.statistics_pages.current_card',
             'mnemosyne.libmnemosyne.statistics_pages.easiness',
             'mnemosyne.libmnemosyne.statistics_pages.grades',
             'mnemosyne.libmnemosyne.statistics_pages.retention_score',
             'mnemosyne.libmnemosyne.statistics_pages.schedule',
             'mnemosyne.libmnemosyne.study_modes.cram_all',
             'mnemosyne.libmnemosyne.study_modes.cram_recent',
             'mnemosyne.libmnemosyne.study_modes.new_only',
             'mnemosyne.libmnemosyne.study_modes.scheduled_forgotten_new',
             'mnemosyne.libmnemosyne.translator',
             'mnemosyne.libmnemosyne.translators.google_translator',
             'mnemosyne.libmnemosyne.ui_components.card_type_widget',
             'mnemosyne.libmnemosyne.ui_components.configuration_widget',
             'mnemosyne.libmnemosyne.ui_components.criterion_widget',
             'mnemosyne.libmnemosyne.ui_components.dialogs',
             'mnemosyne.libmnemosyne.ui_components.main_widget',
             'mnemosyne.libmnemosyne.ui_components.review_widget',
             'mnemosyne.libmnemosyne.ui_components.statistics_widget',
             'mnemosyne.libmnemosyne.upgrades.upgrade1',
             'mnemosyne.libmnemosyne.upgrades.upgrade2',
             'mnemosyne.pyqt_ui.about_dlg',
             'mnemosyne.pyqt_ui.activate_cards_dlg',
             'mnemosyne.pyqt_ui.add_cards_dlg',
             'mnemosyne.pyqt_ui.add_tags_dlg',
             'mnemosyne.pyqt_ui.browse_cards_dlg',
             'mnemosyne.pyqt_ui.card_set_name_dlg',
             'mnemosyne.pyqt_ui.card_type_language_list_wdgt',
             'mnemosyne.pyqt_ui.card_type_tree_wdgt',
             'mnemosyne.pyqt_ui.card_type_wdgt_generic',
             'mnemosyne.pyqt_ui.change_card_type_dlg',
             'mnemosyne.pyqt_ui.clone_card_type_dlg',
             'mnemosyne.pyqt_ui.completion_combo_box',
             'mnemosyne.pyqt_ui.compact_database_dlg',
             'mnemosyne.pyqt_ui.configuration',
             'mnemosyne.pyqt_ui.configuration_dlg',
             'mnemosyne.pyqt_ui.configuration_wdgt_card_appearance',
             'mnemosyne.pyqt_ui.configuration_wdgt_study',
             'mnemosyne.pyqt_ui.configuration_wdgt_main',
             'mnemosyne.pyqt_ui.configuration_wdgt_servers',
             'mnemosyne.pyqt_ui.convert_card_type_keys_dlg',
             'mnemosyne.pyqt_ui.criterion_wdgt_default',
             'mnemosyne.pyqt_ui.delete_unused_media_files_dlg',
             'mnemosyne.pyqt_ui.edit_card_dlg',
             'mnemosyne.pyqt_ui.edit_M_sided_card_type_dlg',
             'mnemosyne.pyqt_ui.edit_M_sided_card_template_wdgt',
             'mnemosyne.pyqt_ui.export_dlg',
             'mnemosyne.pyqt_ui.export_metadata_dlg',
             'mnemosyne.pyqt_ui.getting_started_dlg',
             'mnemosyne.pyqt_ui.import_dlg',
             'mnemosyne.pyqt_ui.main_wdgt',
             'mnemosyne.pyqt_ui.manage_card_types_dlg',
             'mnemosyne.pyqt_ui.manage_plugins_dlg',
             'mnemosyne.pyqt_ui.mnemosyne_rc',
             'mnemosyne.pyqt_ui.mplayer_audio',
             'mnemosyne.pyqt_ui.mplayer_video',
             'mnemosyne.pyqt_ui.prefill_tag_behaviour_plugin',
             'mnemosyne.pyqt_ui.preview_cards_dlg',
             'mnemosyne.pyqt_ui.pronouncer_dlg',
             'mnemosyne.pyqt_ui.pyqt_render_chain',
             'mnemosyne.pyqt_ui.qpushbutton2',
             'mnemosyne.pyqt_ui.qtextedit2',
             'mnemosyne.pyqt_ui.qt_sync_server',
             'mnemosyne.pyqt_ui.qt_gui_translator',
             'mnemosyne.pyqt_ui.qt_web_server',
             'mnemosyne.pyqt_ui.qt_worker_thread',
             'mnemosyne.pyqt_ui.qwebengineview2',
             'mnemosyne.pyqt_ui.remove_tags_dlg',
             'mnemosyne.pyqt_ui.review_wdgt',
             'mnemosyne.pyqt_ui.review_wdgt_cramming',
             'mnemosyne.pyqt_ui.statistics_dlg',
             'mnemosyne.pyqt_ui.statistics_wdgts_plotting',
             'mnemosyne.pyqt_ui.statistics_wdgt_html',
             'mnemosyne.pyqt_ui.sync_dlg',
             'mnemosyne.pyqt_ui.tag_tree_wdgt',
             'mnemosyne.pyqt_ui.translator_dlg',
             'mnemosyne.pyqt_ui.tip_after_starting_n_times',
             'mnemosyne.pyqt_ui.tip_dlg',
             'mnemosyne.pyqt_ui.ui_main_wdgt',
             'mnemosyne.web_server.jquery_mb_html5_audio',
             'mnemosyne.web_server.review_wdgt',
             'mnemosyne.web_server.simple_html5_audio',
             'mnemosyne.web_server.web_server',
             'mnemosyne.web_server.web_server_renderer',
             'mnemosyne.web_server.web_server_render_chain'
]

if sys.platform == 'win32':
             excludes = ['IPython', 'lib2to3']

if sys.platform == 'darwin':
             binaries.append(('/usr/local/bin/mplayer', '.'))
             binaries.append(('/usr/local/lib/libcaca.0.dylib', '.'))
             binaries.append(('/opt/X11/lib/libGL.1.dylib', '.'))
             binaries.append(('/opt/X11/lib/libglut.3.dylib', '.'))
             binaries.append(('/opt/X11/lib/libglapi.0.dylib', '.'))
             binaries.append(('/opt/X11/lib/libXdamage.1.dylib', '.'))
             binaries.append(('/opt/X11/lib/libXfixes.3.dylib', '.'))
             binaries.append(('/opt/X11/lib/libXxf86vm.1.dylib', '.'))
             binaries.append(('/opt/X11/lib/libXi.6.dylib', '.'))
             binaries.append(('/opt/X11/lib/libXrandr.2.dylib', '.'))
             binaries.append(('/opt/X11/lib/libXrender.1.dylib', '.'))

datas.append((os.path.join('mnemosyne', 'libmnemosyne', 'renderers', 'anki', 'hooks.py'), 'anki'))
datas.append((os.path.join('mnemosyne', 'libmnemosyne', 'renderers', 'anki', 'lang.py'), 'anki'))
datas.append((os.path.join('mnemosyne', 'libmnemosyne', 'renderers', 'anki', 'utils.py'), 'anki'))
datas.append((os.path.join('mnemosyne', 'libmnemosyne', 'renderers', 'anki', 'decorator.py'), 'anki'))
datas.append((os.path.join('mnemosyne', 'libmnemosyne', 'renderers', 'anki', '__init__.py'), 'anki'))
datas.append((os.path.join('mnemosyne', 'libmnemosyne', 'renderers', 'anki', 'template', 'furigana.py'),
             os.path.join('anki', 'template')))
datas.append((os.path.join('mnemosyne', 'libmnemosyne', 'renderers', 'anki', 'template', 'hint.py'),
             os.path.join('anki', 'template')))
datas.append((os.path.join('mnemosyne', 'libmnemosyne', 'renderers', 'anki', 'template', 'template.py'),
             os.path.join('anki', 'template')))
datas.append((os.path.join('mnemosyne', 'libmnemosyne', 'renderers', 'anki', 'template', 'view.py'),
             os.path.join('anki', 'template')))
datas.append((os.path.join('mnemosyne', 'libmnemosyne', 'renderers', 'anki', 'template', '__init__.py'),
             os.path.join('anki', 'template')))

a = Analysis([os.path.join('mnemosyne', 'pyqt_ui', 'mnemosyne')],
             pathex=[os.getcwd()],
             binaries=binaries,
             datas=datas,
             hiddenimports=hiddenimports,
             hookspath=[],
             runtime_hooks=[],
             excludes=excludes,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             hooksconfig={
              "matplotlib": {
                "backends": "QtAgg",},
              },
             )

# Still seems to pick up PyQt5 somehow, so we remove it manually.

a.datas = [x for x in a.datas if not "qt5" in x[0].lower()]
a.pure = [x for x in a.pure if not "qt5" in x[0].lower()]
a.zipped_data = [x for x in a.zipped_data if not "qt5" in x[0].lower()]

for x in a.datas:
  print("Datas", x[0], "qt5" in x[0].lower())
for x in a.pure:
  print("Pure", x[0], "qt5" in x[0].lower())
for x in a.zipped_data:
  print("Zipped", x[0], "qt5" in x[0].lower())
  
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

codesign_identity = os.environ['CODESIGN_IDENTITY'] \
      if sys.platform == 'darwin' else None

exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='Mnemosyne',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          codesign_identity=codesign_identity,
          icon=os.path.join('pixmaps', 'mnemosyne.ico'))

coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='Mnemosyne')

if sys.platform == 'darwin':
  app = BUNDLE(coll,
               name='Mnemosyne.app',
               icon=os.path.join('pixmaps', 'mnemosyne.icns'),
               info_plist={
                 'LSBackgroundOnly': '0',
                 'NSHighResolutionCapable': 'True'
               },
               bundle_identifier='org.mnemosyne-proj.Mnemosyne')
