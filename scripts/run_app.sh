project_dir=$(cd "$(dirname $0)"/..; pwd)
python ${project_dir}/service/app.py \
  --model_name_or_path model/sikong-alpaca-7b-chinese \
  --max_new_tokens 800
