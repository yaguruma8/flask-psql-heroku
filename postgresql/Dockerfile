FROM postgres:14

# postgresのコマンドラインの日本語化
# データベースのデフォルトのロケールもja_JPに変更
# Debian-based images のみ（alpine版ではできない）
RUN localedef -i ja_JP -c -f UTF-8 -A /usr/share/locale/locale.alias ja_JP.UTF-8
ENV LANG ja_JP.utf8
