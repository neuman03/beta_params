def beta_params_calculater(mu, var):
    alpha = ((mu**2) * (1-mu) * (1/var)) - mu
    beta = (alpha/mu) - alpha
    return alpha, beta
