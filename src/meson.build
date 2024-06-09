pkgdatadir = get_option('prefix') / get_option('datadir') / meson.project_name()
moduledir = pkgdatadir / 'esp_viewer'
gnome = import('gnome')

gnome.compile_resources('esp_viewer',
  'esp_viewer.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').full_path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', get_option('prefix') / get_option('localedir'))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'esp_viewer.in',
  output: 'esp_viewer',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir'),
  install_mode: 'r-xr-xr-x'
)

esp_viewer_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'connect.py',
  'stackgenerator.py',
  'configparser.py',
  'stream.py',
]

install_data(esp_viewer_sources, install_dir: moduledir)
