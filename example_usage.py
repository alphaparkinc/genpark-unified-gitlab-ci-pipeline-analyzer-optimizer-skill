from client import UnifiedGitlabCiPipelineAnalyzerOptimizerClient

def main():
    client = UnifiedGitlabCiPipelineAnalyzerOptimizerClient()
    res = client.optimize_ci_pipeline('stages: [build, test, deploy]')
    print('GitLab CI Optimizer: ' + res['pipeline_analysis_id'] + ' (Executor: ' + res['executor'] + ')')
    print('Syntax Valid: ' + str(res['syntax_valid']) + ' | Parallelized Stages: ' + str(res['stages_parallelized_count']))
    print('Cache Optimization Gain: +' + str(res['cache_hit_optimization_gain_pct']) + '% | Est. Time Saved: ' + str(res['estimated_build_time_reduction_min']) + 'm')
    print('Optimized YAML: ' + res['optimized_gitlab_ci_url'])

if __name__ == '__main__':
    main()
