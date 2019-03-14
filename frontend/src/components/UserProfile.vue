<template>

    <div id="user-profile" class="col-lg-8"><section class="widget"><!----><header class="title"><h1>
        Perfil Usuario
    </h1></header><div class="widgetControls widget-controls"><!----><!----><!----><!----><!---->
        <div id="__BVID__366" role="group" aria-labelledby="__BVID__366__BV_label_" class="b-form-group form-group" label-breakpoint="md">
            <div class="form-row">
                <label id="__BVID__366__BV_label_" for="basic" class="col-sm-3 col-form-label">Nombre Usuario</label>
                <div class="col-sm-9">
                    <input name="simple" type="text" id="basic" class="form-control" aria-required="true" aria-invalid="false"><!----><!----><!----><!----></div></div></div>
        <div id="__BVID__367" role="group" aria-labelledby="__BVID__367__BV_label_" class="b-form-group form-group" label-breakpoint="md">
            <div class="form-row">
                <label id="__BVID__367__BV_label_" for="minlength" class="col-sm-3 col-form-label">
                    Nombre Completo <br></label>
                <div class="col-sm-9">
                    <input data-vv-validate-on="change" name="minlength" type="text" id="minlength" class="form-control" aria-required="true" aria-invalid="false"><!----><!----><!----><!----></div></div></div>
        <div id="__BVID__368" role="group" aria-labelledby="__BVID__368__BV_label_" class="b-form-group form-group" label-breakpoint="md">
            <div class="form-row">
                <label id="__BVID__368__BV_label_" for="email" class="col-sm-3 col-form-label">E-mail</label>
                <div class="col-sm-9">
                    <input name="email" type="text" id="email" class="form-control" aria-required="true" aria-invalid="false" aria-describedby="__BVID__368__BV_description_"><!----><!----><!---->
                </div></div></div>
        <div id="__BVID__369" role="group" aria-labelledby="__BVID__369__BV_label_" class="b-form-group form-group" label-breakpoint="md">
            <div class="form-row">
                <label id="__BVID__369__BV_label_" for="number" class="col-sm-3 col-form-label">Extra1</label>
                <div class="col-sm-9"><input name="number" type="text" id="number" class="form-control" aria-required="true" aria-invalid="false"><!----><!----><!----><!----></div></div></div>
        <div id="__BVID__370" role="group" aria-labelledby="__BVID__370__BV_label_" class="b-form-group form-group" label-breakpoint="md">
            <div class="form-row"><label id="__BVID__370__BV_label_" for="range" class="col-sm-3 col-form-label">Extra2</label>
                <div class="col-sm-9">
                    <input name="range" type="text" id="range" class="form-control" aria-required="true" aria-invalid="false"><!----><!----><!----><!----></div></div></div>
        <div class="form-action">
            <button type="submit" class="btn btn-rounded float-right btn-danger">Validar &amp; Confirmar</button>
            <button type="button" class="btn btn-rounded btn-default">Cancelar</button></div>
    </div></section>


        <div class="widgetBody widget-body ">
            <div id="__BVID__1485" role="group" aria-labelledby="__BVID__1485__BV_label_" class="b-form-group form-group">
                <div class="form-row">
                    <label id="__BVID__1485__BV_label_" for="fileupload2" class="col-sm-4 col-form-label text-right">Falta por arreglar</label>
                    <div class="col-sm-8">
                        <input accept="image/*" id="fileupload2" type="file" name="file" class="display-none"><div class="fileinput fileinput-new fileinput-fix">
                        <div class="fileinput-new rounded-circle">
                            <img class="img-profile" alt="..." src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5v
                  cmcvMjAwMC9zdmciIHdpZHRoPSIxOTEiIGhlaWdodD0iMTQxIj48cmVjdCB3aWR0aD0
                  iMTkxIiBoZWlnaHQ9IjE0MSIgZmlsbD0iI2VlZSIvPjx0ZXh0IHRleHQtYW5jaG9yPS
                  JtaWRkbGUiIHg9Ijk1LjUiIHk9IjcwLjUiIHN0eWxlPSJmaWxsOiNhYWE7Zm9udC13Z
                  WlnaHQ6Ym9sZDtmb250LXNpemU6MTJweDtmb250LWZhbWlseTpBcmlhbCxIZWx2ZXRp
                  Y2Esc2Fucy1zZXJpZjtkb21pbmFudC1iYXNlbGluZTpjZW50cmFsIj4xOTF4MTQxPC9
                  0ZXh0Pjwvc3ZnPg=="></div></div><div>
                        <button type="button" class="btn mt-sm btn-default">
                            <label for="fileupload2">Select image</label></button></div>
                        <!----><!----><!----></div></div></div></div>

    </div>

</template>

<script>
    export default {
        name: "UserProfile"
    }
</script>

