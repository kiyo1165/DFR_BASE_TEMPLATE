# DFR_BASE_TEMPLATE
## 概要
DFR,CustomUserModel, JWT認証の基本機能 

## インストール
1. DBはPostgresを使用しているため、必要に応じて変更してください。
2. DB設定後
3. python manage.py makemigrations
4. python manage.py migrate
5. to enjoy

## ライブラリ
Pipfileを参照

## セキュリティーについて
django-envronをインストールしているので、必要に応じて環境変数でデータを保護してください。

## Model
### CustomUser
* ユーザー登録時の要件
* Email
* password

### Profile
* One to One フィールドでCustomUserModelに紐付いています。





