project_dir=$(cd "$(dirname $0)"/..; pwd)
python ${project_dir}/app.py \
--model_or_url_path model/sikong-alpaca-7b-chinese \
--max_new_tokens 800