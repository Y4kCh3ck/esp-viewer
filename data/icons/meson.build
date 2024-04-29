# application_id = 'esp_viewer.yackcheck.io'

# scalable_dir = 'hicolor' / 'scalable' / 'apps'
# install_data(
#   scalable_dir / ('@0@.svg').format(application_id),
#   install_dir: get_option('datadir') / 'icons' / scalable_dir
# )

# symbolic_dir = 'hicolor' / 'symbolic' / 'apps'
# install_data(
#   symbolic_dir / ('@0@-symbolic.svg').format(application_id),
#   install_dir: get_option('datadir') / 'icons' / symbolic_dir
# )

icon_themes = ['hicolor']
foreach theme : icon_themes
  install_subdir(theme, install_dir: 'share/icons/')
endforeach