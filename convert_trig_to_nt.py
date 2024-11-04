import rdflib
import isodate

# Dataset object documentation: https://rdflib.readthedocs.io/en/stable/apidocs/rdflib.html#rdflib.graph.Dataset
def run(input_file, output_path, target_graph=1):
    counter = 0
    d = rdflib.Dataset()
    try:
        d.parse(
            input_file,
            format="trig",
            publicID=d.default_context.identifier
            )
        list(d.graphs())[target_graph].serialize(output_path, format="nt")

    except isodate.isoerror.ISO8601Error:
        counter +=1
        print(f"{counter}: ISO8601Error error couured")

if  __name__ == '__main__':
    run("nmvw_data/dhaka-test.trig", "nmvw_data/dhaka-test.nt", 1)