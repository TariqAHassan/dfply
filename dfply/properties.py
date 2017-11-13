from .base import *


@dfpipe
def dim(df):
    """

    Args:
        df:

    Returns:

    """
    return df.shape


@dfpipe
def columns(df):
    """

    Args:
        df:

    Returns:

    """
    return df.columns


@dfpipe
def glimpse(df):
    """

    Args:
        df:

    Returns:

    """
    def elem_to_str(x):
        if isinstance(x, (float, np.floating)):
            return str(round(x, 2))
        else:
            return str(x)

    def arr_to_str(arr):
        head = ", ".join(map(elem_to_str, arr))
        return "{}...".format(head[:79])

    glip = df.dtypes.reset_index()
    glip["summary"] = pd.Series(
        map(arr_to_str, df.head(100).T.values)).values
    glip.index = glip["index"].values
    glip = glip.drop("index", 1).rename(
        columns={0: "dtype", "summary": ""})

    print(glip)
    print("\n[{} x {}]".format(*df.shape))
