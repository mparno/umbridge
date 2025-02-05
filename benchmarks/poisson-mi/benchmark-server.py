import umbridge
import scipy.stats

class Benchmark(umbridge.Model):
    def __init__(self, model_url):
        self.model = umbridge.HTTPModel(model_url)
        self.artificial_truth = [-0.5, 1.5, 1.0, -1.0]
        self.artificial_data = self.model([self.artificial_truth])[0]

    def get_input_sizes(self):
        return self.model.get_input_sizes()

    def get_output_sizes(self):
        return [1]

    def __call__(self, parameters, config={}):
        output = self.model(parameters, config)[0]
        print(output)
        posterior = scipy.stats.multivariate_normal.logpdf(output, self.artificial_data, 1e-4)# \
#                    + scipy.stats.multivariate_normal.logpdf(parameters[0], [0,0,0,0], 5)  # logpdf args: x, loc, scale
        return [[posterior]]

    def supports_evaluate(self):
        return True

benckmark = Benchmark("http://localhost:4242")

umbridge.serve_model(benckmark, 4243)
