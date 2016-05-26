from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from database_control import get_454_sample_reads
from database_control import get_miseq_sample_reads
from database_control import validate_run_id
from database_control import find_454_or_miseq
from flask import request

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def get_run_id():
    return render_template('404.html')
    # return render_template('start.html')


@app.route('/show', methods=["POST"])
def call_454_miseq():
    run_id = request.form['run_id']
    if request.method == 'POST' and validate_run_id(run_id):
        machine_id = find_454_or_miseq(run_id)

        if machine_id[0].__str__() in ['5', '7', '12']:
            sample_infos, sum_infos = get_454_sample_reads(run_id)#[0], get_454_sample_reads(run_id)[1]

            return render_template(
                '454_show_reads.html',
                sample_infos=sample_infos,
                sum_infos = sum_infos
            )
        elif machine_id[0].__str__() in ['11', '14', '15', '20']:
            sample_infos, sum_infos = get_miseq_sample_reads(run_id)#[0], get_miseq_sample_reads(run_id)[1]
            return render_template(
                'miseq_show.html',
                sample_infos=sample_infos,
                sum_infos = sum_infos,
            )
        else:
            return render_template(
                '404.html'
            )
    else:
        return render_template(
            '404.html'
        )


if __name__ == '__main__':
    app.run(debug=True)
