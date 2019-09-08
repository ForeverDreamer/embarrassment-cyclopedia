<template>
	<view>
		<view class="view-box" hover-class="view-box-hover animated rubberBand" hover-stay-time="800">
			这是view
		</view>
		<text :selectable="true">这是text\n这是text\n这是text\n这是text\n这是text\n</text>
	</view>
	
</template>

<script>
	export default {
		data() {
			return {
				
			}
		},
		methods: {
			
		}
	}
</script>

<style>
.view-box {
	width: 200upx;
	height: 200upx;
	background: #007AFF;
	color: #FFFFFF;
	margin: 100upx;
}
.view-box-hover {
	background: red;
}
</style>
