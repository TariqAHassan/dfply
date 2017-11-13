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
    return tuple(df.columns)


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
        return "{}...".format(head[:76])

    glimpse_df = df.dtypes.reset_index()
    glimpse_df["summary"] = pd.Series(
        map(arr_to_str, df.head(100).T.values)).values
    glimpse_df.index = glimpse_df["index"].values
    glimpse_df = glimpse_df.drop("index", 1).rename(
        columns={0: "dtype", "summary": ""})

    print(glimpse_df)
    print("\n[{} x {}]".format(*df.shape))
