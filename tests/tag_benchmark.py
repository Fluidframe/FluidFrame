import timeit
from jinja2 import Template
from fluidframe.core import div


def run_jinja():
    template = Template("""
    <div id="{{ id }}" class="{{ cls }}">
        <div id="{{ id }}" class="{{ cls }}"></div>
    </div>
    """)
    template.render(id="this is id", cls="this is class")

def run_ff_tags():
    div(
        div(id="this is id", cls="this is class"), 
        id="this is id", cls="this is class"
    )
    
def run_jinja_loop():
    template = Template("""
    <div id="{{ id }}" class="{{ cls }}">
        {% for i in range(10000) %}
        <div id="{{ id }}" class="{{ cls }}"></div>
        {% endfor %}
    </div>
    """)
    template.render(id="this is id", cls="this is class")

def run_ff_tags_loop():
    div(
        [div(id="this is id", cls="this is class") for _ in range(10000)], 
        id="this is id", cls="this is class"
    )

def benchmark(func, iteration=1000000):
    tt=[]
    def check_speed(func, *args, **kwargs):
        start_time = timeit.default_timer()
        for i in range(iteration):
            result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        tt.append(end_time - start_time)
        return result
    for _ in range(10):
        check_speed(func)
    return (sum(tt)/len(tt))

if __name__=="__main__":
    #################
    # Tags win here # 
    #################
    iteration = 10000
    # Cython implementation of fluidframe tags
    print(f"Average render time for fluidframe tags: {benchmark(run_ff_tags, iteration)} seconds")

    # Jinja2 templating
    print(f"Average render time for jinja2 templates: {benchmark(run_jinja, iteration)} seconds")
    
    
    ####################
    # Jinja2 wins here # 
    ####################
    iteration = 100
    # Cython implementation of fluidframe tags
    print(f"Average render time for fluidframe tags: {benchmark(run_ff_tags_loop, iteration)} seconds")

    # Jinja2 templating
    print(f"Average render time for jinja2 templates: {benchmark(run_jinja_loop, iteration)} seconds")
    


