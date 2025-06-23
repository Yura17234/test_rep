import argparse
from test_module.config import Config
from test_module.postprocessing.aggregate_results import aggregate_results

def main():
    parser = argparse.ArgumentParser(description="Aggregate PTM search results")
    parser.add_argument('--config', type=str, default='pipeline.cfg', help='Path to config file')
    args = parser.parse_args()

    config = Config(args.config)
    print('Run aggregate result !')
    # print(config.experiment_name)
    # print(config.analysis_index)
    # print(config.search_mode)
    # print(config.fdr_strategy)
    # print(config.fasta_path)
    # print(config.work_dir)
    # print(config.base_config_path)
    aggregate_results(config)
